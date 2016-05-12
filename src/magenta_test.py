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

	def test_MagentaImage_string(self):
		mImage = MagentaImage(1, 1, 2)
		expected = "---MagentaImage---\nRaw dimensions: (1x1)\nScaled dimensions: (2x2) scale=2"
		self.assertEqual(str(mImage), expected)
		mImage = MagentaImage(10, 5, 1)
		expected = "---MagentaImage---\nRaw dimensions: (10x5)\nScaled dimensions: (10x5) scale=1"
		self.assertEqual(str(mImage), expected)

	def test_MagentaImage_argvalidation(self):
		failed = False
		try:
			mImage = MagentaImage(20, 20, "bug")
		except ValueError:
			failed = True
		self.assertEqual(failed, True)

		failed = False
		try:
			mImage = MagentaImage(20, 20, "bug")
		except ValueError:
			failed = True
		self.assertEqual(failed, True)

		failed = False
		try:
			mImage = MagentaImage(20, 20, 5)
		except ValueError:
			failed = True
		self.assertEqual(failed, False)

	def test_MagentaImage_rawsize(self):
		mImage = MagentaImage(20, 20, 4)
		self.assertEqual(mImage.get_rawsize(), (20, 20))

	def test_MagentaImage_scaledsize(self):
		mImage = MagentaImage(20, 10, 5):
		self.assertEqual(mImage.get_scaledsize(), (100, 50))

		
unittest.main()
