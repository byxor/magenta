# magenta
Procedurally generate neat little pixelated images in python3!

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

# Create your image object
rawsize = (64, 64)	# Raw dimensions of the image (before upscaling)
scale = 2			# How much you want to upscale it
image = MagentaImage(rawsize, scale)

# Generate 2 random colours and draw 3 random shapes
palette = generate_pallete(2)
image.draw_random(palette, 3)

# Display your work of art!
image.show()

# Save your work of art!
image.save("magenta.png", "png")

```
