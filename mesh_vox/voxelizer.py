import argparse
import os.path
import numpy

from . import mesh_slice
from . import stl_reader
from . import perimeter
from .util import padVoxelArray


def read_and_reshape_stl(inputFilePath, resolution):
    """
    Read stl file and reshape mesh
    """
    mesh = list(stl_reader.read_stl_verticies(inputFilePath))
    (scale, shift, bounding_box) = mesh_slice.calculateScaleAndShift(mesh, resolution)
    mesh = list(mesh_slice.scaleAndShiftMesh(mesh, scale, shift))
    return (mesh, bounding_box)


def voxelize(mesh, bounding_box, padding=True):
    """
    Voxelize a mesh with a given bounding box
    """
    # Note: voxels should be addressed with voxels[z][x][y]
    voxels = numpy.zeros((bounding_box[2], bounding_box[
                         0], bounding_box[1]), dtype=bool)
    for height in range(bounding_box[2]):
        print('Processing layer %d/%d' % (height+1, bounding_box[2]))
        lines = mesh_slice.toIntersectingLines(mesh, height)
        prepixel = numpy.zeros((bounding_box[0], bounding_box[1]), dtype=bool)
        perimeter.linesToVoxels(lines, prepixel)
        voxels[height] = prepixel
    if padding:
        voxels, bounding_box = padVoxelArray(voxels)
    return (voxels, bounding_box)


def to_ascii(voxels, bounding_box, outputFilePath):
    """
    Create an ascii file and store the voxel array
    """
    output = open(outputFilePath, 'w')
    for z in bounding_box[2]:
        for x in bounding_box[0]:
            for y in bounding_box[1]:
                if voxels[z][x][y]:
                    output.write('%s %s %s\n' % (x, y, z))
    output.close()


if __name__ == '__main__':
    # parse cli args
    parser = argparse.ArgumentParser(description='Convert STL files to voxels')
    parser.add_argument('input', nargs='?')
    parser.add_argument('output', nargs='?')
    parser.add_argument('resolution', nargs='?', type=int)
    args = parser.parse_args()
    # read and rescale
    mesh, bounding_box = read_and_reshape_stl(args.input, args.resolution)
    # create voxel array
    voxels, bounding_box = voxelize(mesh, bounding_box)
    #store the result
    to_ascii(voxels, bounding_box, args.output)
