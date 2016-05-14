from mag_queue import Queue


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


def drawline(mImage, start, end, colour):
	"""Draw a line from A to B on a MagentaImage using DDA Algorithm."""

	x0 = start[0]
	y0 = start[1]
	x1 = end[0]
	y1 = end[1]

	dy = y1-y0
	dx = x1-x0

	steps = None
	if dx > dy:
		steps = abs(dx)
	else:
		steps = abs(dy)

	xIncrement = dx / steps
	yIncrement = dy / steps

	x = x0
	y = y0
	for v in range(0, steps):
		mImage.put_rgb((int(x), int(y)), colour)
		x += xIncrement
		y += yIncrement
