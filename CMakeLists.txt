cmake_minimum_required(VERSION 3.10)
project(PyOpenXr LANGUAGES CXX)

# Keep extraneous variables out of the cmake interface
mark_as_advanced(
    CMAKE_BACKWARDS_COMPATIBILITY
    CMAKE_CONFIGURATION_TYPES
    CMAKE_INSTALL_PREFIX
    EXECUTABLE_OUTPUT_PATH
    LIBRARY_OUTPUT_PATH
)

message(STATUS CMAKE_SYSTEM_NAME = "${CMAKE_SYSTEM_NAME}")

option(PYOPENXR_BUILD_BINDINGS "Generate pyopenxr bindings" OFF)
# Option to control doc build
option(PYOPENXR_BUILD_DOCS "Build Sphinx documentation" OFF)
option(PYOPENXR_BUILD_API_LAYER "Build OpenXR API layer" ON)

# Use local python venv if available
foreach(VENV_DIR "${CMAKE_SOURCE_DIR}/.venv" "$ENV{HOME}/pyopenxr-venv")
    if(EXISTS "${VENV_DIR}")
        set(ENV{VIRTUAL_ENV} "${VENV_DIR}")
        set(Python_FIND_VIRTUALENV ONLY)
    endif()
endforeach()
find_package(Python COMPONENTS Interpreter REQUIRED)
message(STATUS "python = ${Python_EXECUTABLE}")

# TODO: better check for android cross build
if (CMAKE_SYSTEM_PROCESSOR MATCHES "^armv")
    set(ANDROID_ABI arm64-v8a CACHE STRING "")
    set(ANDROID_PLATFORM android-21 CACHE STRING "")
    set(CROSS_COMPILE_ROOT_PATH
        "$ENV{HOME}/android/cpython/cross-build/aarch64-linux-android/prefix/"
        CACHE PATH ""
    )
endif()

if (WIN32)
    set(XR_ARCH "win32")
elseif(ANDROID_ABI MATCHES "arm64")
    set(XR_ARCH "aarch64")
else()
    set(XR_ARCH "x86_64")
endif()
message(STATUS "XR_ARCH = ${XR_ARCH}")

if (CROSS_COMPILE_ROOT_PATH)
    list(APPEND CMAKE_FIND_ROOT_PATH ${CROSS_COMPILE_ROOT_PATH})
endif()

message(STATUS "CMAKE_FIND_ROOT_PATH = ${CMAKE_FIND_ROOT_PATH}")

# Workaround for trouble parsing $ENV{ProgramFiles(x86)}
set(PF86 "ProgramFiles(x86)")

find_path(OPENXR_INCLUDE_DIR
    NAMES openxr/openxr.h
    HINTS
        "$ENV{${PF86}}/OPENXR"
        "$ENV{ProgramW6432}/OPENXR"
        "$ENV{ProgramFiles}/OPENXR"
        "/usr/local"
    PATH_SUFFIXES include
    DOC "The file location of the OpenXR C header files"
)

include_directories(${OPENXR_INCLUDE_DIR})

if (PYOPENXR_BUILD_BINDINGS)
    add_subdirectory(src/generate)
endif()

if (PYOPENXR_BUILD_API_LAYER)
    add_subdirectory(src/generate/py_api_layer)
endif()

# Docs build logic
if(PYOPENXR_BUILD_DOCS)
    # Add a custom target that depends on the core generation
    add_custom_target(docs ALL
        COMMAND ${Python_EXECUTABLE} -m sphinx -b html ${CMAKE_SOURCE_DIR}/src/docs ${CMAKE_SOURCE_DIR}/docs
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
        COMMENT "Generating Sphinx documentation"
        VERBATIM
    )
    # add_dependencies(docs xrg_generate) # Replace xrg_generate with the actual target name
endif()
