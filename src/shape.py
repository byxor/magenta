import abc

class Shape(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def draw(self, mImage, position, size):
		return


class Rect(Shape):

	def draw(self, mImage, pos, size, colour):
		"""Draws a rectangle on the provided MagentaImage, at the specified
		raw_position, with the specified size, with the specified colour. The
		drawn shape is upscaled based on the MagentaImage's scale attribute."""

		xpos = pos[0]
		ypos = pos[1]
		width = size[0]
		height = size[1]
		for x in range(xpos, xpos+width):
			for y in range(ypos, ypos+width):
				mImage.put_scaledpixel((x, y), colour)


shapes = [Rect]
