#from distutils.core import setup
from setuptools import setup
from distutils.extension import Extension
#from setuptools import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

# setup.py file
import sys
import os
import shutil


# clean previous build
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if (name.startswith("civy") and not(name.endswith(".pyx") or name.endswith(".pxd"))):
            os.remove(os.path.join(root, name))
    for name in dirs:
        if (name == "build"):
            pass
           #shutil.rmtree(name)

inc_dirs = [os.getcwd(), 'freeciv/utility', 'freeciv/gen_headers', 'freeciv/common', 'freeciv/common/networking', 'freeciv/server', 'freeciv/common/aicore',
       #'/usr/local/include',
       #'/usr/include'
        ]
depends = [#'freeciv/utility/log.h', 'freeciv/server/srv_main.h', './freeciv/common/game.h',
       #'/usr/include/bzlib.h'
        ]
sourcefiles = ['civy.pyx',#'freeciv/common/game.c', 'freeciv/utility/log.c', 'freeciv/utility/deprecations.c'
        ]
extensions = [
        Extension('civy', 
            sourcefiles, 
            include_dirs=inc_dirs,
            libraries=['freeciv'],
            extra_compile_args=["-fopenmp", 
                "-O3"],
            extra_link_args=["-DSOME_DEFINE_OPT", 
                               "-L/usr/include"
                              #'-framework', 'BZ'
                               ]
            )]
setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules=cythonize(extensions,
            compiler_directives={'language_level': "3"}),
        )
