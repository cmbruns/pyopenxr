cmake_minimum_required(VERSION 3.10)
project(PyOpenXr LANGUAGES CXX)

option(PYOPENXR_BUILD_BINDINGS "Generate pyopenxr bindings" OFF)
# Option to control doc build
option(PYOPENXR_BUILD_DOCS "Build Sphinx documentation" OFF)

# Use local python venv if available
foreach(VENV_DIR "${CMAKE_SOURCE_DIR}/.venv" "$ENV{HOME}/pyopenxr-venv")
    if(EXISTS "${VENV_DIR}")
        set(ENV{VIRTUAL_ENV} "${VENV_DIR}")
        set(Python_FIND_VIRTUALENV ONLY)
    endif()
endforeach()
find_package(Python COMPONENTS Interpreter REQUIRED)
message("python = ${Python_EXECUTABLE}")

if (PYOPENXR_BUILD_BINDINGS)
    add_subdirectory(src/generate)
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
