import random


def generate_colour(influence=(0,0,0)):
    """Generates a random (r, g, b) tuple. The influence allows you to set the
	lower boundary of each colour channel. E.g. (50, 0, 0) would force Red
	to be within the range of 50 to 256."""
    r = influence[0] + random.randrange(256-influence[0])
    g = influence[1] + random.randrange(256-influence[1])
    b = influence[2] + random.randrange(256-influence[2])
    return (r, g, b)


def generate_palette(size, influence=(0,0,0)):
    """Generates a random colour palette."""
    palette = []
    for i in range(0, size):
        colour = generate_colour(influence)
        palette.append(colour)
    return palette
