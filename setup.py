#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mesh_vox',
      version='0.1.0',
      description='Mesh Voxelizer, turn your 3D model to voxels',
      author='Christian Pedersen, Sonny Lion',
      author_email='',
      url='https://github.com/Septaris/mesh_vox',
      packages=find_packages(exclude=('tests',)),
     )