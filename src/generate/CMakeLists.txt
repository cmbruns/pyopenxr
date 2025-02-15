cmake_minimum_required(VERSION 3.10)
cmake_policy(SET CMP0177 NEW)
project(PyOpenXr LANGUAGES CXX)

message(STATUS "This Configure step creates updated version bindings for pyopenxr")

option(PYOPENXR_OVERWRITE_CURRENT_SOURCE_FILES "Overwrite current source files?" OFF)

set(PYOPENXR_VERSION_PATCH_INCREMENTAL 1
    CACHE STRING "PyOpenXR incremental patch version (usually 1)")
set(PYOPENXR_VERSION_SUFFIX "a"
    CACHE STRING "PyOpenXR version suffix (empty string for official releases, 'a' for pre-releases)")

# Keep extraneous variables out of the cmake interface
mark_as_advanced(
    CMAKE_BACKWARDS_COMPATIBILITY
    CMAKE_CONFIGURATION_TYPES
    CMAKE_INSTALL_PREFIX
    EXECUTABLE_OUTPUT_PATH
    LIBRARY_OUTPUT_PATH
)

# Workaround for trouble parsing $ENV{ProgramFiles(x86)}
set(PF86 "ProgramFiles(x86)")

# TODO: add more hints for Mac and Linux
find_path(OPENXR_INCLUDE_DIR
    NAMES openxr/openxr.h
    HINTS
        "$ENV{${PF86}}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
    PATH_SUFFIXES include
    DOC "The file location of the OpenXR C header files"
)

include_directories(${OPENXR_INCLUDE_DIR})

set(OPENXR_INCLUDE_FILE "${OPENXR_INCLUDE_DIR}/openxr/openxr.h")
if (EXISTS "${OPENXR_INCLUDE_FILE}")
    file(COPY "${OPENXR_INCLUDE_DIR}/openxr/" DESTINATION "${CMAKE_CURRENT_SOURCE_DIR}/xrg/headers")
endif()

######################

find_file(OPENXR_REGISTRY_FILE
    NAMES xr.xml
    HINTS
        "$ENV{USERPROFILE}/Documents/git"
        "$ENV{HOME}/git"
    PATH_SUFFIXES OpenXR-SDK-Source/specification/registry
    DOC "The file location of the OpenXR registry file (xr.xml)"
)
if (OPENXR_REGISTRY_FILE)
    configure_file(
        "${OPENXR_REGISTRY_FILE}"
        "${CMAKE_CURRENT_SOURCE_DIR}/xrg/headers"
        COPYONLY
    )
endif()

####################################
### Find libclang shared library ###
####################################

find_file(LIBCLANG_SHARED_LIBRARY
    NAMES libclang.dll libclang.so libclang.dylib
    HINTS
        "$ENV{ProgramW6432}/LLVM"
        "$ENV{ProgramFiles}/LLVM"
        "/usr/lib/llvm-14/lib"
        "/usr/lib/llvm-10/lib"
    PATH_SUFFIXES bin
    DOC "The 64-bit(?) libclang shared library file (https://releases.llvm.org/download.html)"
)
if (EXISTS "${LIBCLANG_SHARED_LIBRARY}")
    get_filename_component(LIBCLANG_NAME ${LIBCLANG_SHARED_LIBRARY} NAME)
    # Use COPY_FILE to copy real file not just symlink
    configure_file("${LIBCLANG_SHARED_LIBRARY}" "${CMAKE_CURRENT_SOURCE_DIR}/xrg/${LIBCLANG_NAME}" COPYONLY)
endif()

# Create staging folder for generated source files
set(STAGING_DIR "${CMAKE_BINARY_DIR}/xr")
file(MAKE_DIRECTORY "${STAGING_DIR}")
file(MAKE_DIRECTORY "${STAGING_DIR}/platform")
file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/platform")

###########################
### Generate version.py ###
###########################

find_package(Python COMPONENTS Interpreter REQUIRED)

message(STATUS "Python Executable = " ${Python_EXECUTABLE})
execute_process(
    COMMAND ${Python_EXECUTABLE} print_openxr_version.py
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    OUTPUT_VARIABLE OPENXR_VERSION
)
message(STATUS "OpenXR Version = ${OPENXR_VERSION}")

#########################################
### Copy openxr_loader shared library ###
#########################################

find_file(OPENXR_LOADER_SHARED_LIBRARY
    NAMES openxr_loader.dll libopenxr_loader.so libopenxr_loader.dylib
    HINTS
        "${OPENXR_INCLUDE_DIR}/.."
        "$ENV{${PF86}}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
    PATH_SUFFIXES x64/bin bin lib
    DOC "The openxr_loader shared library file"
)
if (OPENXR_LOADER_SHARED_LIBRARY)
    file(MAKE_DIRECTORY "${STAGING_DIR}/library")
    configure_file("${OPENXR_LOADER_SHARED_LIBRARY}" "${STAGING_DIR}/library" COPYONLY)
    message(STATUS "Copied openxr_loader shared library to ${STAGING_DIR}/library/")
endif()

############################
# Copy prebuilt api layers #
############################

find_file(OPENXR_VALIDATION_LAYER_JSON
    NAMES XrApiLayer_core_validation.json
    HINTS
        "${OPENXR_INCLUDE_DIR}/.."
        "$ENV{${PF86}}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
        "/usr/local/share/openxr/1/api_layers/explicit.d/"
    PATH_SUFFIXES x64/bin/api_layers bin/api_layers lib
    DOC "Pre-built validation API layer for packaging"
)
find_file(OPENXR_VALIDATION_LAYER_LIB
    NAMES libXrApiLayer_core_validation.so XrApiLayer_core_validation.dll
    HINTS
        "${OPENXR_INCLUDE_DIR}/.."
        "$ENV{${PF86}}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
        "/usr/local/lib"
    PATH_SUFFIXES x64/bin/api_layers bin/api_layers lib
    DOC "Pre-built validation API layer for packaging"
)
foreach (LAYER_FILE ${OPENXR_VALIDATION_LAYER_JSON} ${OPENXR_VALIDATION_LAYER_LIB})
    if (LAYER_FILE)
        file(MAKE_DIRECTORY "${STAGING_DIR}/api_layer")
        if (WIN32)
            set(API_LAYER_OUTPUT_FOLDER "${STAGING_DIR}/api_layer/windows")
        else()
            set(API_LAYER_OUTPUT_FOLDER "${STAGING_DIR}/api_layer/linux")
        endif()
        get_filename_component(LAYERS_INPUT ${LAYER_FILE} DIRECTORY)
        file(GLOB API_LAYER_JSONS  RELATIVE "${LAYERS_INPUT}" "${LAYERS_INPUT}/XrApiLayer*.json")
        if (WIN32)
            file(GLOB API_LAYER_LIBS  RELATIVE "${LAYERS_INPUT}" "${LAYERS_INPUT}/XrApiLayer*.dll")
        else()
            file(GLOB API_LAYER_LIBS  RELATIVE "${LAYERS_INPUT}" "${LAYERS_INPUT}/libXrApiLayer*.so")
        endif()
        file(MAKE_DIRECTORY "${API_LAYER_OUTPUT_FOLDER}")
        foreach(F ${API_LAYER_JSONS})
            file(COPY "${LAYERS_INPUT}/${F}" DESTINATION "${API_LAYER_OUTPUT_FOLDER}")
        endforeach()
        foreach(F ${API_LAYER_LIBS})
            file(COPY "${LAYERS_INPUT}/${F}" DESTINATION "${API_LAYER_OUTPUT_FOLDER}")
        endforeach()
        # file(COPY "${API_LAYER_JSONS}" DESTINATION "${API_LAYER_OUTPUT_FOLDER}")
        # file(COPY "${API_LAYER_LIBS}" DESTINATION "${API_LAYER_OUTPUT_FOLDER}")
        message(STATUS "Copied api layer files to ${API_LAYER_OUTPUT_FOLDER}")
    endif()
endforeach()

##################################
### Generate enums source file ###
##################################

function(generate_source GENERATOR OUTPUT OUT_DIR)
    # Two step copy so newlines are used as line ending
    execute_process(
        COMMAND ${Python_EXECUTABLE} "${GENERATOR}"
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
        OUTPUT_FILE "${CMAKE_BINARY_DIR}/${OUTPUT}"
    )
    configure_file(
        "${CMAKE_BINARY_DIR}/${OUTPUT}"
        "${STAGING_DIR}/${OUT_DIR}/"
        @ONLY
        NEWLINE_STYLE LF  # Even/especially on windows...
    )
    message(STATUS "Generated file ${STAGING_DIR}/${OUTPUT}")
endfunction()

set(ENV{PYTHONPATH} "${CMAKE_CURRENT_SOURCE_DIR}")
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/generate_version.py ${CMAKE_CURRENT_BINARY_DIR}/ @ONLY)
generate_source("${CMAKE_CURRENT_BINARY_DIR}/generate_version.py" "version.py" "")

generate_source("generate_enums.py" "enums.py" "")
generate_source("generate_constants.py" "constants.py" "")
generate_source("generate_typedefs.py" "typedefs.py" "")
generate_source("generate_raw_functions.py" "raw_functions.py" "")
generate_source("generate_functions.py" "functions.py" "")
if(WIN32)
    generate_source("generate_windows_platform.py" "windows.py" "platform")
else()
    generate_source("generate_linux_platform.py" "linux.py" "platform")
endif()
generate_source("generate_exceptions.py" "exception.py" "")

##########################################
### Find OpenXR-Registry documentation ###
##########################################

string(REPLACE "." ";" OPENXR_VERSION_LIST ${OPENXR_VERSION})
list(GET OPENXR_VERSION_LIST 0 OPENXR_VERSION_MAJOR)
list(GET OPENXR_VERSION_LIST 1 OPENXR_VERSION_MINOR)
list(GET OPENXR_VERSION_LIST 2 OPENXR_VERSION_PATCH)
set(HTML_DIR "specs/${OPENXR_VERSION_MAJOR}.${OPENXR_VERSION_MINOR}/man/html")

find_path(OPENXR_REGISTRY_PATH
    NAMES "${HTML_DIR}/openxr.html"
    HINTS
        "$ENV{USERPROFILE}/Documents/git/OpenXR-Registry"
        "$ENV{HOME}/git/OpenXR-Registry"
    DOC "The file location of the OpenXR-Registry source code"
)

######################################
### Final install into source tree ###
######################################

if (PYOPENXR_OVERWRITE_CURRENT_SOURCE_FILES)
   message(STATUS "")
   message(WARNING "Warning: Overwriting contents of source xr package.")
   file(COPY "${CMAKE_BINARY_DIR}/xr/" DESTINATION "${CMAKE_SOURCE_DIR}/../xr/")
endif()

add_subdirectory(py_api_layer)
