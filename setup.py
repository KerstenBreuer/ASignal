#!/usr/bin/env python3
import os
from setuptools import find_packages, setup

SETUP_DIR = os.path.dirname(__file__)
README = os.path.join(SETUP_DIR, 'README.rst')

setup(
    name='asignal',
    version='0.0.1',    
    description='Generates signal tracks for investigating chromatin accessibility, transcriptions factor profiling, and nucleosome positions based on ATAC-seq Data',
    long_description=open(README).read(),
    long_description_content_type="text/x-rst",
    url='https://github.com/KerstenBreuer/ASignal',
    download_url="https://github.com/KerstenBreuer/ASignal",
    author='Kersten Henrik Breuer',
    author_email='k.breuer@dkfz.de',
    license='Apache 2.0',
    include_package_data=True,
    packages=find_packages(exclude=("experimental")),
    entry_points={
        "console_scripts": [
            "asignal=asignal.__main__:main",
        ]
    },
    install_requires=[              
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX', 
        'Operating System :: POSIX :: Linux',    
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 8.1', 
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)