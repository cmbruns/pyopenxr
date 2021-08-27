project(GeneratePyOpenXr LANGUAGES NONE)
cmake_minimum_required(VERSION 2.8.12)

message(STATUS "This Configure step creates updated version bindings for pyopenxr")

option(PYOPENXR_OVERWRITE_CURRENT_SOURCE_FILES "Overwrite current source files?" OFF)
set(PYOPENXR_VERSION_PATCH_INCREMENTAL 1
    CACHE STRING "PyOpenXR incremental patch version (usually 1)")

# Keep extraneous variables out of the cmake interface
mark_as_advanced(
    CMAKE_BACKWARDS_COMPATIBILITY
    CMAKE_CONFIGURATION_TYPES
    CMAKE_INSTALL_PREFIX
    EXECUTABLE_OUTPUT_PATH
    LIBRARY_OUTPUT_PATH
)

# TODO: add more hints for Mac and Linux
find_path(OPENXR_INCLUDE_DIR
    NAMES openxr/openxr.h
    HINTS
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
    PATH_SUFFIXES include
    DOC "The file location of the OpenXR C header files"
)

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
    PATH_SUFFIXES OpenXR-SDK/specification/registry
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
    PATH_SUFFIXES bin
    DOC "The 64-bit(?) libclang shared library file (https://releases.llvm.org/download.html)"
)
if (EXISTS "${LIBCLANG_SHARED_LIBRARY}")
    get_filename_component(LIBCLANG_NAME ${LIBCLANG_SHARED_LIBRARY} NAME)
    # Use COPY_FILE to copy real file not just symlink
    file(COPY_FILE "${LIBCLANG_SHARED_LIBRARY}" "${CMAKE_CURRENT_SOURCE_DIR}/xrg/${LIBCLANG_NAME}")
endif()

# Create staging folder for generated source files
set(STAGING_DIR "${CMAKE_BINARY_DIR}/xr")
file(MAKE_DIRECTORY "${STAGING_DIR}")
file(MAKE_DIRECTORY "${STAGING_DIR}/platform")
file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/platform")

###########################
### Generate version.py ###
###########################

find_package(PythonInterp)

execute_process(
    COMMAND ${PYTHON_EXECUTABLE} print_openxr_version.py
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
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
    PATH_SUFFIXES bin lib
    DOC "The openxr_loader shared library file"
)
if (OPENXR_LOADER_SHARED_LIBRARY)
    file(MAKE_DIRECTORY "${STAGING_DIR}/library")
    configure_file("${OPENXR_LOADER_SHARED_LIBRARY}" "${STAGING_DIR}/library" COPYONLY)
    message(STATUS "Copied openxr_loader shared library to ${STAGING_DIR}/library/")
endif()

##################################
### Generate enums source file ###
##################################

function(generate_source GENERATOR OUTPUT OUT_DIR)
    # Two step copy so newlines are used as line ending
    execute_process(
        COMMAND ${PYTHON_EXECUTABLE} "${GENERATOR}"
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

generate_source("generate_version.py" "version.py" "")
generate_source("generate_enums.py" "enums.py" "")
generate_source("generate_constants.py" "constants.py" "")
generate_source("generate_typedefs.py" "typedefs.py" "")
generate_source("generate_raw_functions.py" "raw_functions.py" "")
generate_source("generate_functions.py" "functions.py" "")
generate_source("generate_windows_platform.py" "windows.py" "platform")
generate_source("generate_exceptions.py" "exceptions.py" "")

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
