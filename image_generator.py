from PIL import Image
import numpy as np

# Create a random 10x10 pixel image
random_image = np.random.randint(0, 256, (50, 50, 3), dtype=np.uint8)  # Generating random pixel values
random_image = Image.fromarray(random_image, 'RGB')  # Convert numpy array to PIL Image

# Save the image as a JPEG file
random_image.save('random_image.jpg')

# Optionally, display the image
random_image.show()