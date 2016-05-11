from PIL import Image
import random

def generate_colour():
    """Generates a random (r, g, b) tuple."""
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r, g, b)


def generate_palette(size):
    """Generates a random colour palette."""
    palette = []
    for i in range(0, size):
        colour = generate_colour()
        palette.append(colour)
    return palette


def new_image(width, height, scale):
    """Returns a blank new RGB image."""
    mode = "RGB"
    dimensions = (width*scale, height*scale)
    fill_colour = (0, 0, 0)
    return Image.new(mode, dimensions, fill_colour)
