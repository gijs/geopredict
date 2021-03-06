import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="geopredict",
    version="0.0.1",
    author="Matthew Perry",
    author_email="perrygeo@gmail.com",
    description=("Utilities for applying scikit-learn to spatial datasets"),
    license="BSD",
    keywords="gis geospatial geographic raster vector zonal statistics machinelearning",
    url="https://github.com/perrygeo/geopredict",
    package_dir={'': 'src'},
    packages=['geopredict'],
    long_description=read('README.md'),
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'GDAL',
    ],
    #tests_require=['pytest', 'pyshp>=1.1.4', 'coverage'],
    #cmdclass = {'test': PyTest},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
