#from distutils.core import setup
from setuptools import setup
from Cython.Build import cythonize
from setuptools import Extension
#from distutils.extension import Extension
import os

inc_dirs = [os.getcwd(), './utility', 'gen_headers', 'common', 'common/networking', './server',
        'common/aicore']
depends = ['./utility/log.h', 'server/srv_main.h', './common/game.h']
sourcefiles = ['civy.pyx', #'common/game.c', 'utility/log.c', 'utility/deprecations.c'
        ]
extensions = [Extension('civy', sourcefiles, include_dirs=inc_dirs)]
setup(
    cmdclass = {'build_ext': build_ext},
        ext_modules=cythonize(extensions))
