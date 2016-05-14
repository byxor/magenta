
def generate_colour(influence=(0,0,0)):
    """Generates a random (r, g, b) tuple. The influence allows you to set the
	lower boundary of each colour channel. E.g. (50, 0, 0) would force Red
	to be within the range of 50 to 256."""
    r = influence + random.randrange(256-influence)
    g = influence + random.randrange(256-influence)
    b = influence + random.randrange(256-influence)
    return (r, g, b)


def generate_palette(size, influence=(0,0,0)):
    """Generates a random colour palette."""
    palette = []
    for i in range(0, size):
        colour = generate_colour(influence)
        palette.append(colour)
    return palette
