from PIL import Image
import random

class MagentaImage(object):

	def __init__(self, raw_width, raw_height, scale):
		"""Constructor for MagentaImage."""
		self._raw_width = raw_width
		self._raw_height = raw_height
		self._scale = scale
		self.__init_image

	def __init_image(self):
		"""Creates the PIL image for the MagentaImage object. Do not call."""
		MODE = "RGB"
		w = self._raw_width * self._scale
		h = self._raw_height * self._scale
		DIMS = (w, h)
		FILL = (0, 0, 0)
		self.__image = Image.new(MODE, DIMS, FILL)

	def __str__(self):
		s = "---MagentaImage---\n"
		s += "Raw dimensions: ({}x{})\n".format(self._raw_width, self._raw_height)
		s += "Scaled dimensions: ({}x{}) scale={}".format(self.get_scaledwidth(), self.get_scaledheight(), self._scale)
		return s

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
