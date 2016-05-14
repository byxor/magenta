from queue import Queue

def floodfill(mImage, root, fill):
	"""Iteratively floodfill a MImage."""

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
