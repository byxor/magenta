from PIL import Image
import random

class MagentaImage(object):

	def __init__(self, raw_width, raw_height, scale=1):
		"""Constructor for MagentaImage."""
		MagentaImage.__check_args(raw_width, raw_height, scale)
		self.__raw_width = raw_width
		self.__raw_height = raw_height
		self.__scale = scale
		self.__init_image()

	@staticmethod
	def __check_args(raw_width, raw_height, scale):
		"""Validates the args passed to the constructor."""
		if str(type(raw_width)) != "<class 'int'>":
			raise ValueError("'raw_width' must be of type 'int'.")
		if str(type(raw_height)) != "<class 'int'>":
			raise ValueError("'raw_height' must be of type 'int'.")
		if str(type(scale)) != "<class 'int'>":
			raise ValueError("'scale' must be of type 'int'.")
		if raw_width <= 0:
			raise ValueError("'raw_width' must be greater than 0.")
		if raw_height <= 0:
			raise ValueError("'raw_height' must be greater than 0.")
		if scale <= 0:
			raise ValueError("'scale' must be greater than 0.")

	def __init_image(self):
		"""Creates the PIL image for the MagentaImage object. Do not call."""
		w = self.__raw_width * self.__scale
		h = self.__raw_height * self.__scale
		MODE = "RGB"
		DIMS = (w, h)
		FILL = (0, 0, 0)
		self.__image = Image.new(MODE, DIMS, FILL)

	def __str__(self):
		"""Returns string representation of MagentaImage instance."""
		s = "---MagentaImage---\n"
		rawsize = self.get_rawsize()
		s += "Raw dimensions: ({:d}x{:d})\n".format(rawsize[0], rawsize[1])
		scaledsize = self.get_scaledsize()
		scw = scaledsize[0]
		sch = scaledsize[1]
		s += "Scaled dimensions: ({:d}x{:d}) scale={:d}".format(scw, sch, self.__scale)
		return s

	def get_rawsize(self):
		"""Gets the dimensions of the image before scaling is applied."""
		return (self.__raw_width, self.__raw_height)

	def get_scaledsize(self):
		"""Gets the dimensions of the upscaled image."""
		return self.__image.size

	def show(self):
		"""Displays the image (mainly for debugging). Check the PIL Image.show()
		documentation to find out more."""
		self.__image.show()

	def save(self, filepath, format=None, **params):
		"""Saves the MagentaImage to a file. Check the PIL Image.save()
		documentation to find out more."""
		self.__image.save(filepath, format, params)


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
