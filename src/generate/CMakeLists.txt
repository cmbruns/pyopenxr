message(STATUS "This Configure step creates updated version bindings for pyopenxr")

option(PYOPENXR_OVERWRITE_CURRENT_SOURCE_FILES "Overwrite current source files?" OFF)

set(PYOPENXR_VERSION_PATCH_INCREMENTAL 1
    CACHE STRING "PyOpenXR incremental patch version (usually 1)")
set(PYOPENXR_VERSION_SUFFIX "a"
    CACHE STRING "PyOpenXR version suffix (empty string for official releases, 'a' for pre-releases)")

# TODO: Maybe auto update OpenXR-SDK-Source repo
find_path(OPENXR_SDK_SOURCE_REPO_PATH
    NAMES src/tests/hello_xr
    HINTS
        "${CMAKE_SOURCE_DIR}/../OpenXR-SDK-Source"
    CMAKE_FIND_ROOT_PATH_BOTH
    DOC "The file location of the OpenXR-SDK-Source local git repo"
)
if (OPENXR_SDK_SOURCE_REPO_PATH)
    # Set desired version behavior: AS-IS, LATEST, or a specific tag like release-1.1.50
    set(OPENXR_TAG_SELECTION "AS-IS" CACHE STRING
    "Set desired version behavior: AS-IS, LATEST, or a specific tag like release-1.1.50")
    set_property(CACHE OPENXR_TAG_SELECTION PROPERTY STRINGS "AS-IS" "LATEST")
    
    # Fetch latest tags from origin
    execute_process(
        COMMAND git fetch --tags
        WORKING_DIRECTORY "${OPENXR_SDK_SOURCE_REPO_PATH}"
        RESULT_VARIABLE FETCH_RESULT
    )
    if(NOT FETCH_RESULT EQUAL 0)
        message(WARNING "Failed to fetch tags from origin.")
    endif()
    
    # Get all release tags
    execute_process(
        COMMAND git tag --list release-*
        WORKING_DIRECTORY "${OPENXR_SDK_SOURCE_REPO_PATH}"
        OUTPUT_VARIABLE RELEASE_TAGS_RAW
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    string(REPLACE "\n" ";" RELEASE_TAGS "${RELEASE_TAGS_RAW}")
    list(SORT RELEASE_TAGS ORDER DESCENDING)
    list(GET RELEASE_TAGS 0 LATEST_TAG)
    message(STATUS "Latest OpenXR-SDK-Source release tag is ${LATEST_TAG}")
    
    # Get current HEAD tag (if any)
    execute_process(
        COMMAND git describe --tags --exact-match
        WORKING_DIRECTORY "${OPENXR_SDK_SOURCE_REPO_PATH}"
        OUTPUT_VARIABLE CURRENT_TAG
        RESULT_VARIABLE DESCRIBE_RESULT
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    
    # Determine desired tag based on selection
    set(DESIRED_TAG "")
    if(OPENXR_TAG_SELECTION STREQUAL "LATEST")
        set(DESIRED_TAG "${LATEST_TAG}")
    elseif(OPENXR_TAG_SELECTION STREQUAL "AS-IS")
        set(DESIRED_TAG "${CURRENT_TAG}")  # No checkout; preserve current
    else()
        set(DESIRED_TAG "${OPENXR_TAG_SELECTION}")  # Use explicit tag
    endif()
    
    # Checkout logic
    if(NOT DESIRED_TAG STREQUAL "${CURRENT_TAG}" AND NOT OPENXR_TAG_SELECTION STREQUAL "AS-IS")
        message(STATUS "Switching to desired OpenXR-SDK-Source release tag: ${DESIRED_TAG}")
        execute_process(
            COMMAND git checkout "${DESIRED_TAG}"
            WORKING_DIRECTORY "${OPENXR_SDK_SOURCE_REPO_PATH}"
            RESULT_VARIABLE CHECKOUT_RESULT
        )
        if(CHECKOUT_RESULT EQUAL 0)
            message(STATUS "Switched to ${DESIRED_TAG}")
        else()
            message(WARNING "Failed to switch to ${DESIRED_TAG}. It may not exist.")
        endif()
    else()
        message(STATUS "Repo already at desired release tag: ${DESIRED_TAG}")
    endif()
endif()

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
    CMAKE_FIND_ROOT_PATH_BOTH
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
        # "/usr/lib/llvm-14/lib"
        "/usr/lib/llvm-10/lib"
        "/usr/lib/llvm-12/lib"
    PATH_SUFFIXES bin
    NO_CMAKE_FIND_ROOT_PATH
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

message(STATUS "Python Executable = " ${Python_EXECUTABLE})
execute_process(
    COMMAND ${Python_EXECUTABLE} print_openxr_version.py
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    OUTPUT_VARIABLE OPENXR_VERSION
)
message(STATUS "OpenXR Version = ${OPENXR_VERSION}")

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
    CMAKE_FIND_ROOT_PATH_BOTH
    DOC "The file location of the OpenXR-Registry source code"
)

if (OPENXR_REGISTRY_PATH)
    # Fetch latest tags from origin
    execute_process(
        COMMAND git fetch --tags
        WORKING_DIRECTORY "${OPENXR_REGISTRY_PATH}"
        RESULT_VARIABLE FETCH_RESULT
    )
    if(NOT FETCH_RESULT EQUAL 0)
        message(WARNING "Failed to fetch tags from origin.")
    endif()

    # Get all release tags
    execute_process(
        COMMAND git tag --list release-*
        WORKING_DIRECTORY "${OPENXR_REGISTRY_PATH}"
        OUTPUT_VARIABLE RELEASE_TAGS_RAW
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    string(REPLACE "\n" ";" RELEASE_TAGS "${RELEASE_TAGS_RAW}")
    list(SORT RELEASE_TAGS ORDER DESCENDING)
    list(GET RELEASE_TAGS 0 LATEST_TAG)
    message(STATUS "Latest OpenXR-Registry release tag is ${LATEST_TAG}")

    # Get current HEAD tag (if any)
    execute_process(
        COMMAND git describe --tags --exact-match
        WORKING_DIRECTORY "${OPENXR_REGISTRY_PATH}"
        OUTPUT_VARIABLE CURRENT_TAG
        RESULT_VARIABLE DESCRIBE_RESULT
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )

    # Determine desired tag based on selection
    set(DESIRED_TAG "")
    if(OPENXR_TAG_SELECTION STREQUAL "LATEST")
        set(DESIRED_TAG "${LATEST_TAG}")
    elseif(OPENXR_TAG_SELECTION STREQUAL "AS-IS")
        set(DESIRED_TAG "${CURRENT_TAG}")  # No checkout; preserve current
    else()
        set(DESIRED_TAG "${OPENXR_TAG_SELECTION}")  # Use explicit tag
    endif()

    # Checkout logic
    if(NOT DESIRED_TAG STREQUAL "${CURRENT_TAG}" AND NOT OPENXR_TAG_SELECTION STREQUAL "AS-IS")
        message(STATUS "Switching to desired OpenXR-Registry release tag: ${DESIRED_TAG}")
        execute_process(
            COMMAND git checkout "${DESIRED_TAG}"
            WORKING_DIRECTORY "${OPENXR_REGISTRY_PATH}"
            RESULT_VARIABLE CHECKOUT_RESULT
        )
        if(CHECKOUT_RESULT EQUAL 0)
            message(STATUS "Switched to ${DESIRED_TAG}")
        else()
            message(WARNING "Failed to switch to ${DESIRED_TAG}. It may not exist.")
        endif()
    else()
        message(STATUS "Repo already at desired release tag: ${DESIRED_TAG}")
    endif()
endif()

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
    file(MAKE_DIRECTORY "${STAGING_DIR}/library/${XR_ARCH}")
    configure_file("${OPENXR_LOADER_SHARED_LIBRARY}" "${STAGING_DIR}/library/${XR_ARCH}" COPYONLY)
    message(STATUS "Copied openxr_loader shared library to ${STAGING_DIR}/library/${XR_ARCH}")
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
    PATH_SUFFIXES bin/api_layers lib
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
        set(API_LAYER_OUTPUT_FOLDER "${STAGING_DIR}/api_layer/${XR_ARCH}")
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
    message(STATUS "  generating file ${CMAKE_BINARY_DIR}/${OUTPUT}")
    execute_process(
        COMMAND ${Python_EXECUTABLE} "${GENERATOR}"
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
        OUTPUT_FILE "${CMAKE_BINARY_DIR}/${OUTPUT}"
    )
    message(STATUS "  copying file ${STAGING_DIR}/${OUTPUT}")
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
    # generate_source("generate_android_platform.py" "android.py" "platform")
else()
    generate_source("generate_linux_platform.py" "linux.py" "platform")
    generate_source("generate_android_platform.py" "android.py" "platform")
endif()
generate_source("generate_exceptions.py" "exception.py" "")

######################################
### Final install into source tree ###
######################################

if (PYOPENXR_OVERWRITE_CURRENT_SOURCE_FILES)
   message(STATUS "")
   message(WARNING "Warning: Overwriting contents of source xr package.")
   file(COPY "${CMAKE_BINARY_DIR}/xr/" DESTINATION "${CMAKE_SOURCE_DIR}/src/xr/")
endif()
