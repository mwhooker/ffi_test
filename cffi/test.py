from cffi import FFI
ffi = FFI()

ffi.cdef(open('hello.h').read())
lib = ffi.dlopen('./libhello.so')
#lib = ffi.verify("#include <hello.h>", include_dirs=["."])

a = ffi.string(lib.hello())
print a
