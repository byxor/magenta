from queue import Queue


def floodfill(mImage, root, fill):
	"""Iteratively floodfill a MagentaImage."""

	old_colour = mImage.get_rgb(root)
	q = Queue()
	q.enqueue(root)

	while q.size() > 0:

		pos = q.dequeue()
		if mImage.get_rgb(pos) != old_colour:
			continue

		mImage.put_rgb(pos, fill)
		q.enqueue((pos[0]+0, pos[1]-1))	# Enqueue the northern cell
		q.enqueue((pos[0]+1, pos[1]+0))	# Enqueue the eastern cell
		q.enqueue((pos[0]+0, pos[1]+1))	# Enqueue the southern cell
		q.enqueue((pos[0]-1, pos[1]+0))	# Enqueue the wester cell


def line(mImage, start, end, colour):
	"""Draw a line from A to B on a MagentaImage."""

	x1 = start[0]
	y1 = start[1]

	x2 = start[0]
	y2 = start[1]

	dy = y2 - y1
	dx = x2 - x1

	for x in range(x1, x2):
		y = y1 + dy * (x - x1) / dx
		mImage.put_rgb((x,y), colour)
