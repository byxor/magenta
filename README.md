# magenta
Procedurally generate neat little pixelated images in python3!

## Dependencies

Magenta depends on a few libraries which can easily be installed with pip...

`pip install libjpeg-dev`  
`pip install zlib1g-dev`  
`pip install Pillow`  

## Usage
Want to generate a cool image? Here's how...  
```
from magenta import *

# Create your image object
raw_width = 100		# Width of the image
raw_height = 100	# Height of the image
scale = 2					# How much you want to upscale it
image = MagentaImage(raw_width, raw_height, scale)

# Generate 3 random colours and draw a random pattern
palette = generate_pallete(3)
image.draw_random(palette)

# Display your work of art!
image.show()
```
