import clang

# These variables are filled in by cmake's configure_file process
OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

