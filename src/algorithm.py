import structure

def i_floodfill(mImage, root, fill):
	"""Iteratively floodfill a MagentaImage."""

	old_colour = mImage.get_rgb(root)
	q = structure.Queue()
	q.enqueue(root)

	while q.size() > 0:

		pos = q.dequeue()

		print("Processing ({}, {})".format(pos[0], pos[1]))

		if mImage.get_rgb(pos) != old_colour:
			continue

		mImage.put_rgb(pos, fill)

		north = (pos[0]+0, pos[1]-1)
		east = (pos[0]+1, pos[1]+0)
		south = (pos[0]+0, pos[1]+1)
		west = (pos[0]-1, pos[1]+0)
		q.enqueue(north)
		q.enqueue(east)
		q.enqueue(south)
		q.enqueue(west)


def r_floodfill(mImage, old_col, new_col, pos):
	"""Recursively floodfill a MagentaImage."""

	if mImage.get_rgb(pos) != old_col:
		return

	mImage.put_rgb(pos, new_col)

	r_floodfill(mImage, old_col, new_col, (pos[0]+0, pos[1]-1))
	r_floodfill(mImage, old_col, new_col, (pos[0]+1, pos[1]+0))
	r_floodfill(mImage, old_col, new_col, (pos[0]+0, pos[1]+1))
	r_floodfill(mImage, old_col, new_col, (pos[0]-1, pos[1]+0))


def squiggle(mImage, frm, dirs):
	import random
	x = frm[0]
	y = frm[1]
	while True:
		if mImage.get_rgb((x, y)) in [None, (0, 0, 0)]:
			return
		mImage.put_rgb((x, y), (0, 0, 0))
		nextdir = random.choice(dirs)
		x += nextdir[0]
		y += nextdir[1]
