project(PyOpenXRAndroid)
cmake_minimum_required(VERSION 2.8.12)

set(ANDROID_ABI arm64-v8a CACHE STRING "")
set(ANDROID_PLATFORM android-21 CACHE STRING "")

add_library(XrApiLayer_python_android SHARED ../py_api_layer/py_api_layer.cpp)
set_target_properties(XrApiLayer_python_android PROPERTIES
    OUTPUT_NAME XrApiLayer_python
    LINK_FLAGS "-Wl,-Bsymbolic,--exclude-libs,ALL"
)
target_include_directories(XrApiLayer_python_android PRIVATE /usr/local/include)
install(TARGETS XrApiLayer_python_android
    DESTINATION ${CMAKE_SOURCE_DIR}../../../xr/api_layer/android
)
