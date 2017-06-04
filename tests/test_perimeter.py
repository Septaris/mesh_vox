import random
import numpy
import unittest

import mesh_vox.mesh_slice as mesh_slice
from mesh_vox.util import printBigArray
import mesh_vox.perimeter as perimeter

class PerimeterTest(unittest.TestCase):


    def test_cross_line(self):
        self.assertTrue(perimeter.onLine([(0,0,0),(2,2,0)],1,1))
        self.assertTrue(perimeter.onLine([(2,2,0),(0,0,0)],1,1))
        self.assertFalse(perimeter.onLine([(2,2,0),(0,0,0)],2,1))
        self.assertFalse(perimeter.onLine([(2,2,0),(0,0,0)],1,2))
        self.assertTrue(perimeter.onLine([(0,0,0),(4,2,0)],2,1))

if __name__ == '__main__':
    unittest.main()
