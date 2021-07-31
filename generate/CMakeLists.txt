project(GeneratePyOpenXr LANGUAGES NONE)
cmake_minimum_required(VERSION 2.8.12)

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
        "$ENV{ProgramFiles}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
    PATH_SUFFIXES include
    DOC "The file location of the OpenXR C header files"
)

set(OPENXR_INCLUDE_FILE "${OPENXR_INCLUDE_DIR}/openxr/openxr.h")

find_package(PythonInterp)

configure_file(generate_version.py.in
    ${CMAKE_BINARY_DIR}/generate_version.py @ONLY)

execute_process(
    COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_BINARY_DIR}/generate_version.py"
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}"
    RESULT_VARIABLE py_result
)
message(STATUS "Generated file ${STAGING_DIR}/version.py")

#############################
### Copied shared library ###
#############################

find_file(OPENXR_LOADER_SHARED_LIBRARY
    NAMES openxr_loader.dll openxr_loader.so openxr_loader.dylib
    HINTS
        "${OPENXR_INCLUDE_DIR}/.."
        "$ENV{ProgramFiles}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
    PATH_SUFFIXES bin
    DOC "The openxr_loader shared library file"
)
if (OPENXR_LOADER_SHARED_LIBRARY)
    file(MAKE_DIRECTORY "${STAGING_DIR}/library")
    configure_file("${OPENXR_LOADER_SHARED_LIBRARY}" "${STAGING_DIR}/library" COPYONLY)
    message(STATUS "Copied openxr_loader shared library to ${STAGING_DIR}/library/")
endif()

if (PYOPENXR_OVERWRITE_CURRENT_SOURCE_FILES)
   message(WARNING "Overwriting contents of xr folder")
   file(COPY "${CMAKE_BINARY_DIR}/xr/" DESTINATION "${CMAKE_SOURCE_DIR}/xr/")
endif()

# I think one more blank line looks nice
message(STATUS "")
