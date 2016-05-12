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
from shape import *

# Create your image object
rawsize = (32, 32) # Raw dimensions of the image.
image = MagentaImage(rawsize, scale=2) # Scale of 2 upscales the image to 64x64.

# Generate 5 random colours and draw 30 random shapes
palette = generate_palette(size=5)
image.draw_random(palette, shapes, complexity=30)

# Display your work of art!
image.show()

# Save your work of art!
image.save("magenta.png", "png")

```
