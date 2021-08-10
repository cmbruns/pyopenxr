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

# Create staging folder for generated source files
set(STAGING_DIR "${CMAKE_BINARY_DIR}/xr")
file(MAKE_DIRECTORY "${STAGING_DIR}")

###########################
### Generate version.py ###
###########################

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

find_package(PythonInterp)

# Helper files for generate_whatever.py
file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/xrg")
configure_file(xrg/__init__.py ${CMAKE_BINARY_DIR}/xrg @ONLY)

configure_file(print_openxr_version.py ${CMAKE_BINARY_DIR}/ @ONLY)
execute_process(
    COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_BINARY_DIR}/print_openxr_version.py"
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}"
    OUTPUT_VARIABLE OPENXR_VERSION
)
message(STATUS "OpenXR Version = ${OPENXR_VERSION}")

#########################################
### Copy openxr_loader shared library ###
#########################################

find_file(OPENXR_LOADER_SHARED_LIBRARY
    NAMES openxr_loader.dll openxr_loader.so openxr_loader.dylib
    HINTS
        "${OPENXR_INCLUDE_DIR}/.."
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
    PATH_SUFFIXES bin
    DOC "The openxr_loader shared library file"
)
if (OPENXR_LOADER_SHARED_LIBRARY)
    file(MAKE_DIRECTORY "${STAGING_DIR}/library")
    configure_file("${OPENXR_LOADER_SHARED_LIBRARY}" "${STAGING_DIR}/library" COPYONLY)
    message(STATUS "Copied openxr_loader shared library to ${STAGING_DIR}/library/")
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

##################################
### Generate enums source file ###
##################################

function(generate_source GENERATOR OUTPUT)
    configure_file("${GENERATOR}" "${CMAKE_BINARY_DIR}/" @ONLY)
    # Two step copy so newlines are used as line ending
    execute_process(
        COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_BINARY_DIR}/${GENERATOR}"
        WORKING_DIRECTORY "${STAGING_DIR}"
        OUTPUT_FILE "${CMAKE_BINARY_DIR}/${OUTPUT}"
    )
    configure_file(
        "${CMAKE_BINARY_DIR}/${OUTPUT}"
        "${STAGING_DIR}/"
        @ONLY
        NEWLINE_STYLE LF  # Even on windows...
    )
    message(STATUS "Generated file ${STAGING_DIR}/${OUTPUT}")
endfunction()

generate_source("generate_version.py" "version.py")
generate_source("generate_enums.py" "enums.py")
generate_source("generate_constants.py" "constants.py")
generate_source("generate_typedefs.py" "typedefs.py")
generate_source("generate_raw_functions.py" "raw_functions.py")

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
   message(WARNING "Warning: Overwriting contents of source xr package. Are you authoring a new release of pyopenxr?")
   file(COPY "${CMAKE_BINARY_DIR}/xr/" DESTINATION "${CMAKE_SOURCE_DIR}/../xr/")
endif()

# I think one more blank line looks nice
message(STATUS "")
