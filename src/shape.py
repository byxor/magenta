#TODO: Replace abstract class Shape with Drawable interface.

class Shape(object):

	@abstractmethod
	def draw(self, mImage, position, size):
		pass


class Square(Shape):

	def draw(self, mImage, position, size):
		pass
