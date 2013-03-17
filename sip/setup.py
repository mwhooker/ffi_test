from distutils.core import setup, Extension
import sipdistutils


setup (
    name = 'test',
    version = '1.0',
    description = 'This is a demo package',
    ext_modules=[
        Extension("test", ["test.sip", "test.c"]),
    ],
    cmdclass = {'build_ext': sipdistutils.build_ext}
)
