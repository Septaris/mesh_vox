import unittest
import random
import numpy

import mesh_vox.mesh_slice as mesh_slice
import mesh_vox.stl_reader as stl_reader
from mesh_vox.util import printBigArray


class TestSlice(unittest.TestCase):

    def testIsAboveAndBelow(self):
        tri = (
            [1, 2, 5],
            [2, 3, 4],
            [3, 2, 1]
        )
        self.assertTrue(mesh_slice.isAboveAndBelow(tri, 4))
        # self.assertTrue(mesh_slice.isAboveAndBelow(tri, 5))
        # self.assertTrue(mesh_slice.isAboveAndBelow(tri, 1))
        self.assertFalse(mesh_slice.isAboveAndBelow(tri, 5.5))
        self.assertFalse(mesh_slice.isAboveAndBelow(tri, 0))

    def testIsAboveAndBelow_inclusive(self):
        tri = [
            [1, 2, 5],
            [2, 3, 5],
            [3, 2, 1]
        ]
        self.assertTrue(mesh_slice.isAboveAndBelow(tri, 5))

    def test_wherelinecrossesz(self):
        p1 = [2., 4., 1.]
        p2 = [1., 2., 5.]
        self.assertEqual(mesh_slice.whereLineCrossesZ(p1, p2, 1), tuple(p1))
        self.assertEqual(mesh_slice.whereLineCrossesZ(p1, p2, 5), tuple(p2))
        self.assertEqual(mesh_slice.whereLineCrossesZ(p1, p2, 3), (1.5, 3, 3))
        self.assertEqual(mesh_slice.whereLineCrossesZ([0, 0, 0], [0, 1, 1], 0.5), (0.0, 0.5, 0.5))


    def test_linearInterpolation(self):
        p1 = (2, 4, 1)
        p2 = (1, 2, 5)
        p3 = (1.5, 3, 3)
        self.assertEqual(mesh_slice.linearInterpolation(p1, p2, 0), p1)
        self.assertEqual(mesh_slice.linearInterpolation(p1, p2, 1), p2)
        self.assertEqual(mesh_slice.linearInterpolation(p1, p2, .5), p3)


    def test_triangleToIntersectingLines(self):
        tri = [
            [2, 4, 1],
            [1, 2, 5],
            [3, 2, 3]
        ]
        lines = list(mesh_slice.triangleToIntersectingLines(tri, 4))
        # self.assertIn((tri[0], tri[1]), lines)
        # self.assertIn((tri[2], tri[1]), lines)
        print(lines)
        self.assertEqual(2, len(lines))

    # def test_triangleToIntersectingLines_onePointSame(self):
    #     tri = [
    #         [2, 4, 1],
    #         [1, 2, 5],
    #         [3, 2, 3]
    #     ]
    #     lines = list(mesh_slice.triangleToIntersectingLines(tri, 3))
    #     self.assertTrue((tri[0], tri[2]) in lines or (tri[2], tri[1]) in lines)

    # def test_triangleToIntersectingLines_twoPointSame(self):
    #     tri = [
    #         [2, 4, 3],
    #         [1, 2, 5],
    #         [3, 2, 3]
    #     ]
    #     lines = list(mesh_slice.triangleToIntersectingLines(tri, 3))
    #     self.assertTrue((tri[0], tri[1]) in lines or (tri[2], tri[1]) in lines)

    # def test_triangleToIntersectingLines_threePointSame(self):
    #     tri = [
    #         [2, 4, 3],
    #         [1, 2, 3],
    #         [3, 2, 3]
    #     ]
    #     lines = list(mesh_slice.triangleToIntersectingLines(tri, 3))
    #     self.assertTrue(tri in lines)


if __name__ == '__main__':
    unittest.main()