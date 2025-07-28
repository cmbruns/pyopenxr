add_library(XrApiLayer_python SHARED py_api_layer.cpp)

if (WIN32)
    install(
        TARGETS XrApiLayer_python
        RUNTIME  # dll only?
        DESTINATION ${CMAKE_SOURCE_DIR}/src/xr/api_layer/windows
    )
else()
    set_target_properties(XrApiLayer_python PROPERTIES LINK_FLAGS "-Wl,-Bsymbolic,--exclude-libs,ALL")
    install(
        TARGETS XrApiLayer_python
        DESTINATION ${CMAKE_SOURCE_DIR}/src/xr/api_layer/linux
    )
endif()
