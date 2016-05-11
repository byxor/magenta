import unittest
from magenta import *

class MagentaTest(unittest.TestCase):

    def test_palette_length(self):
        self.assertEqual( len(generate_palette(2)) , 2 )
        self.assertEqual( len(generate_palette(1)) , 1 )
        self.assertEqual( len(generate_palette(0)) , 0 )
        self.assertEqual( len(generate_palette(100)) , 100 )

    def test_colour_bounds(self):
        colour = generate_colour()
        self.assertLess(colour[0], 256)
        self.assertLess(colour[1], 256)
        self.assertLess(colour[2], 256)
        self.assertGreaterEqual(colour[0], 0)
        self.assertGreaterEqual(colour[1], 0)
        self.assertGreaterEqual(colour[2], 0)

    # def test_
