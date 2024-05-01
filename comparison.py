
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import importlib.util

# Import the Python files for different seam carving algorithms
spec1 = importlib.util.spec_from_file_location("seamcarving", "seamcarving.py")
dynamic = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(dynamic)

spec2 = importlib.util.spec_from_file_location("greedy", "greedy.py")
greedy = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(greedy)


# Load the image
image_path = "random_image.jpg"


# Function to time the execution of each algorithm on the image
def time_algorithms(img, scales):
    times1 = []
    times2 = []
    for scale in scales:
        start_time = time.time()
        dynamic.main2('c', scale, image_path, 'output.jpg')
        end_time = time.time()
        times1.append(end_time - start_time)
        
        start_time = time.time()
        greedy.main2('c', scale, image_path, 'output.jpg')
        end_time = time.time()
        times2.append(end_time - start_time)
    return times1, times2

# Function to plot the runtime of algorithms for the image at different scales
def plot_runtime_vs_scale(scales, times1, times2):
    plt.figure(figsize=(10, 6))
    plt.plot(scales, times1, label='Dynamic Programming')
    plt.plot(scales, times2, label='Greedy')
    plt.title('Runtime Comparison of Algorithms for the Image at Different Scales')
    plt.xlabel('Scale')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function
if __name__ == '__main__':
    scales = [0.25, 0.5, 0.75, 1]  # Add more scales as needed
    times1, times2 = time_algorithms(scales)
    plot_runtime_vs_scale(scales, times1, times2)
'''
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import importlib.util

# Import the Python files for different seam carving algorithms
spec1 = importlib.util.spec_from_file_location("seamcarving", "seamcarving.py")
dynamic = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(dynamic)

spec2 = importlib.util.spec_from_file_location("greedy", "greedy.py")
greedy = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(greedy)

# Function to resize the image
def resize_image(image_path, size):
    img = Image.open(image_path)
    img_resized = img.resize(size, Image.ANTIALIAS)
    img_resized.save('random_image.jpg')

# Function to time the execution of each algorithm on the image
def time_algorithms(sizes):
    times1 = []
    times2 = []
    for size in sizes:
        resize_image(image_path, size)
        
        start_time = time.time()
        dynamic.main2('c', size, image_path, 'output.jpg')
        end_time = time.time()
        times1.append(end_time - start_time)
        
        start_time = time.time()
        greedy.main2('c', size, image_path, 'output.jpg')
        end_time = time.time()
        times2.append(end_time - start_time)
    return times1, times2

# Function to plot the runtime of algorithms for the image at different scales
def plot_runtime_vs_scale(sizes, times1, times2):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times1, label='Dynamic Programming')
    plt.plot(sizes, times2, label='Greedy')
    plt.title('Runtime Comparison of Algorithms for the Image at Different Sizes')
    plt.xlabel('Image Size')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function
if __name__ == '__main__':
    image_path = "random_image.jpg"
    sizes = [(int(1000 * scale), int(1000 * scale)) for scale in [0.25, 0.5, 0.75, 1]]  # Adjust size as needed
    times1, times2 = time_algorithms(sizes)
    plot_runtime_vs_scale(sizes, times1, times2)
'''