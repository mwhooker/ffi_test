 .PHONY : clean build


example.py:
	swig -python example.i
_example.so:
	python setup.py build_ext --inplace

build: example.py _example.so

clean:
	rm example.py example_wrap.c _example.so

