build the shared library

    gcc -c -fPIC hello.c -o hello.o
    gcc -shared -Wl -o libhello.so hello.o

and then run

    python test.py

 and it works
