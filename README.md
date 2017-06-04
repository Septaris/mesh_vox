# Mesh Vox
The mesh voxelizer (Mesh Vox) is a fork of [stl-to-voxel](https://github.com/rcpedersen/stl-to-voxel/). It turns STL files into voxels array. In particular, this library can be used to create [Starmade](https://starmadedock.net/) blueprints from 3D models.

## Installation

Mesh Vox require python 3 and can be installed using pip:
```
pip install git+https://github.com/Septaris/mesh_vox.git
```

## Usage

```python
from mesh_vox import read_and_reshape_stl, voxelize

# path to the stl file
input_path = 'my_stl_file'
# number of voxels used to represent the largest dimension of the 3D model
resolution = 100 

# read and rescale
mesh, bounding_box = read_and_reshape_stl(input_path, resolution)
# create voxel array
voxels, bounding_box = voxelize(mesh, bounding_box)

print(voxels)

```