import unittest
from magenta import *

class MagentaTest(unittest.TestCase):

    def test_generate_palette(self):
        self.assertEqual(len(generate_palette(2)), 2)
        self.assertEqual(len(generate_palette(1)), 1)
        self.assertEqual(len(generate_palette(0)), 0)
        self.assertEqual(len(generate_palette(100)), 100)

    def test_generate_colour(self):
        colour = generate_colour()
        self.assertLess(colour[0], 256)
        self.assertLess(colour[1], 256)
        self.assertLess(colour[2], 256)
        self.assertGreaterEqual(colour[0], 0)
        self.assertGreaterEqual(colour[1], 0)
        self.assertGreaterEqual(colour[2], 0)

    def test_new_image(self):
        self.assertEqual(new_image(10, 15, 2).size, (20, 30))
        self.assertEqual(new_image(10, 15, 3).size, (30, 45))
        self.assertEqual(new_image(16, 16, 10).mode, "RGB")
        self.assertEqual(new_image(1, 1, 1).mode, "RGB")


unittest.main()
