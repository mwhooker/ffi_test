from cffi import FFI
ffi = FFI()
ffi.cdef("""     // some declarations from the man page
     struct passwd {
        char    *pw_shell;
        ...;
    };
    struct passwd *getpwuid(int uid);
""")
C = ffi.verify("""   // passed to the real C compiler
#include <sys/types.h>
#include <pwd.h>
""", libraries=[])   # or a list of libraries to link with
p = C.getpwuid(0)

print ffi.string(p.pw_shell)
