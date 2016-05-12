from PIL import Image
import random


class MagentaImage(object):

	def __init__(self, rawsize, scale=1):
		"""Constructor for MagentaImage."""
		MagentaImage.__check_args(rawsize, scale)
		self.__rawsize = rawsize
		self.__scale = scale
		self.__init_image()

	@staticmethod
	def __check_args(rawsize, scale):
		"""Validates the args passed to the constructor."""
		if str(type(rawsize)) != "<class 'geometry.Dimension'>":
			raise ValueError("'rawsize' must be of type 'Dimension'.")
		if str(type(rawsize.width)) != "<class 'int'>":
			raise ValueError("'raw_width' must be of type 'int'.")
		if str(type(rawsize.height)) != "<class 'int'>":
			raise ValueError("'raw_height' must be of type 'int'.")
		if str(type(scale)) != "<class 'int'>":
			raise ValueError("'scale' must be of type 'int'.")
		if rawsize.width <= 0:
			raise ValueError("'raw_width' must be greater than 0.")
		if rawsize.height <= 0:
			raise ValueError("'raw_height' must be greater than 0.")
		if scale <= 0:
			raise ValueError("'scale' must be greater than 0.")

	def __init_image(self):
		"""Creates the PIL image for the MagentaImage object. Do not call."""
		w = self.__rawsize.width * self.__scale
		h = self.__rawsize.height * self.__scale
		MODE = "RGB"
		SCALED_DIMS = (w, h)
		FILL = (0, 0, 0)
		self.__image = Image.new(MODE, SCALED_DIMS, FILL)

	def __str__(self):
		"""Returns string representation of MagentaImage instance."""
		rawsize = self.get_rawsize()
		scaledsize = self.get_scaledsize()
		s = "---MagentaImage---\n"
		s += "Raw dimensions: ({:d}x{:d})\n"
		s.format(rawsize.width, rawsize.height)
		s += "Scaled dimensions: ({:d}x{:d}) scale={:d}"
		s.format(scaledsize.width, scaledsize.height, self.__scale)
		return s

	def __draw_random_shape(self, palette):
		"""Draws a random shape on the MagentaImage using the palette."""

		# TO DO ...
		# PASS A SHAPE SAMPLE INTO THIS METHOD
		# DEPENDENCY INJECTION

		# Select random colour from palette
		rnd = random.randrange(0, len(palette))
		colour = palette[rnd]
		# Select random shape
		# Select random location/size
		# Draw pattern

	def put_scaledpixel(self, pos, colour):
		"""Takes raw co-ordinates and a colour as arguments and automatically
		draws the pixel in that location (after scaling has been applied)."""

		pos_scaled = Position(pos.x*self.__scale, pos.y*self.__scale)

		for x in range(pos_scaled.x, pos_scaled.x + self.__scale):
			for y in range(pos_scaled.y, pos_Scaled.y + self.__scale):
				self.__image.putpixel((x, y), colour)

	def get_rawsize(self):
		"""Gets the dimensions of the image before scaling is applied."""
		return self.__rawsize

	def get_scaledsize(self):
		"""Gets the dimensions of the upscaled image."""
		return self.__image.size

	def get_scale(self):
		"""Gets the scale of the image."""
		return self.__scale

	def show(self):
		"""Displays the image (mainly for debugging). Check the PIL Image.show()
		documentation to find out more."""
		self.__image.show()

	def save(self, filepath, format=None):
		"""Saves the MagentaImage to a file. Check the PIL Image.save()
		documentation to find out more."""
		self.__image.save(filepath, format)

	def draw_random(self, palette, complexity=3):
		"""Draw random patterns on the image using the provided colour palette.
		The complexity defines the number of shapes to draw."""
		for i in range(0, complexity):
			self.__draw_random_shape(palette)


def generate_colour():
    """Generates a random (r, g, b) tuple."""
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r, g, b)


def generate_palette(size):
    """Generates a random colour palette."""
    palette = []
    for i in range(0, size):
        colour = generate_colour()
        palette.append(colour)
    return palette


def draw_pattern(image, palette):
    """Draws a random pattern onto the specified image using the specified
    palette."""
