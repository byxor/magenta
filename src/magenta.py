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
		if str(type(rawsize[0])) != "<class 'int'>":
			raise ValueError("'raw_width' must be of type 'int'.")
		if str(type(rawsize[1])) != "<class 'int'>":
			raise ValueError("'raw_height' must be of type 'int'.")
		if str(type(scale)) != "<class 'int'>":
			raise ValueError("'scale' must be of type 'int'.")
		if rawsize[0] <= 0:
			raise ValueError("'raw_width' must be greater than 0.")
		if rawsize[1] <= 0:
			raise ValueError("'raw_height' must be greater than 0.")
		if scale <= 0:
			raise ValueError("'scale' must be greater than 0.")

	def __init_image(self):
		"""Creates the PIL image for the MagentaImage object. Do not call."""
		w = self.__rawsize[0] * self.__scale
		h = self.__rawsize[1] * self.__scale
		MODE = "RGB"
		SCALED_DIMS = (w, h)
		FILL = (0, 0, 0)
		self.__image = Image.new(MODE, SCALED_DIMS, FILL)

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

	def __draw_random_shape(self, palette, shapes):
		"""Draws a random shape on the MagentaImage using the palette."""

		rnd = random.randrange(0, len(palette))
		colour = palette[rnd]

		rnd = random.randrange(0, len(shapes))
		shape = shapes[rnd]()

		rndX = random.randrange(-self.get_rawsize()[0], self.get_rawsize()[0])
		rndY = random.randrange(-self.get_rawsize()[1], self.get_rawsize()[1])
		pos = (rndX, rndY)

		rndX = random.randrange(0, self.get_rawsize()[0])
		rndY = random.randrange(0, self.get_rawsize()[1])
		size = (rndX, rndY)

		shape.draw(self, pos, size, colour)


	def put_scaledpixel(self, pos, colour):
		"""Takes raw co-ordinates and a colour as arguments and automatically
		draws the pixel in that location (after scaling has been applied)."""
		rawx = pos[0]
		rawy = pos[1]

		if not 0 <= rawx < self.get_rawsize()[0]:
			return
		if not 0 <= rawy < self.get_rawsize()[1]:
			return

		for x in range(rawx*self.__scale, (rawx+1)*self.__scale):
			for y in range(rawy*self.__scale, (rawy+1)*self.__scale):
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

	def fill(self, colour):
		"""Fills the entire image with a solid colour."""
		for x in range(0, self.get_rawsize()[0]):
			for y in range(0, self.get_rawsize()[1]):
				self.put_scaledpixel((x, y), colour)

	def draw_random(self, palette, shapes, complexity=3):
		"""Draw random patterns on the image using the provided colour palette.
		The complexity defines the number of shapes to draw."""

		self.fill(palette[0])

		for i in range(0, complexity):
			self.__draw_random_shape(palette, shapes)

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
