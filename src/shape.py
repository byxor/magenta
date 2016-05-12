import abc


class Shape(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def draw(self, mImage, position, size):
		return


class Rect(Shape):

	def draw(self, mImage, colour, attributes):
		"""Draws a rectangle on the provided MagentaImage, at the specified
		raw_position, with the specified size, with the specified colour. The
		drawn shape is upscaled based on the MagentaImage's scale attribute."""
		pos = attributes[0]
		dim = attributes[1]
		for x in range(pos.x, pos.x+dim.width):
			for y in range(pos.y, pos.y+dim.height):
				mImage.put_scaledpixel((x, y), colour)
				
