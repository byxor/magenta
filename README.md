# magenta
Procedurally generate neat little pixelated images in python3!

Magenta's design philosophy is simplicity. Let's keep things quick and easy to use.  
A happy API makes a happy programmer.

## Dependencies

Magenta depends on a few libraries which can easily be installed with pip...

```bash
pip install libjpeg-dev  
pip install zlib1g-dev  
pip install Pillow
```

## Usage
Want to generate a cool image? Here's how...  
```python
from magenta import *
from geometry import *

# Create your image object
<<<<<<< HEAD
rawsize = Dimension(32, 32) # Raw dimensions of the image.
image = MagentaImage(rawsize, scale=2) # Scale of 2 upscales the image to 64x64.
=======
raw_width = 100		# Width of the image
raw_height = 100	# Height of the image
scale = 2			# How much you want to upscale it
image = MagentaImage(raw_width, raw_height, scale)
>>>>>>> parent of e23edaa... Update README usage to match new syntax

# Generate 2 random colours and draw 3 random shapes
palette = generate_pallete(2)
image.draw_random(palette, 3)

# Display your work of art!
image.show()

# Save your work of art!
image.save("magenta.png", "png")

```
