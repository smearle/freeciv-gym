# setup.sh
# Make the "freeciv-gym" Python Module ("myext.so")

all:
	CC="/usr/local/opt/llvm/bin/clang"   \
	CXX="g++"   \
	CFLAGS="-I./freeciv/common -I/usr/local/opt/llvm/include -I/usr/local/include -I/opt/X11/include -I/usr/local/Frameworks/Python.framework/Versions/3.7/include"  \
	LDFLAGS="-L/usr/local/lib -L/usr/lib -L/usr/local/opt/llvm/lib"   \
	python3 setup.py build_ext --inplace
