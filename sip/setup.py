from distutils.core import setup, Extension
import sipdistutils


setup (
    name = 'demo',
    version = '1.0',
    description = 'This is a demo package',
    ext_modules=[
        Extension("demo", ["demo.sip", "demo.c"]),
    ],
    cmdclass = {'build_ext': sipdistutils.build_ext}
)
