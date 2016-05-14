from copy import deepcopy

class Queue(object):

	def __init__(self):
		self.__list = []

	def __str__(self):
		s = "["
		for i in range(0, self.size()):
			if i > 0:
				s += ", "
			s += str(self.__list[i])
		s += "]"
		return s

	def size(self):
		return len(self.__list)

	def enqueue(self, element):
		self.__list.append(element)

	def dequeue(self):
		element = deepcopy(self.__list[0])
		self.__list.pop(0)
		return element
