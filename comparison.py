
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import importlib.util
import timeit

# Import the Python files for different seam carving algorithms
spec1 = importlib.util.spec_from_file_location("seamcarving", "seamcarving.py")
dynamic = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(dynamic)

spec2 = importlib.util.spec_from_file_location("greedy", "greedy.py")
greedy = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(greedy)

spec3 = importlib.util.spec_from_file_location("bruteforce", "bruteforce.py")
bruteforce = importlib.util.module_from_spec(spec3)
spec3.loader.exec_module(bruteforce)

spec4 = importlib.util.spec_from_file_location("gpu", "dynamic_gpu.py")
gpu = importlib.util.module_from_spec(spec4)
spec4.loader.exec_module(gpu)

# Load the image
image_path = "random_image.jpg"


# Function to time the execution of each algorithm on the image
def time_algorithms(scales):
    times_dp = []
    times_greedy = []
    times_gpu = []
    times_brute = []
    for scale in scales:
        tm1 = 0
        tm2 = 0
        tm3 = 0
        for i in range(1):
            start_time = time.time()
            dynamic.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm1 += end_time - start_time
            
            start_time = time.time()
            greedy.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm2 += end_time - start_time

            start_time = time.time()
            gpu.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm3 += end_time - start_time
        times_dp.append(tm1/5)
        times_greedy.append(tm2/5)
        times_gpu.append(tm3/5)

    return times_dp, times_greedy, times_gpu



def time_algorithms_b(scales):
    times_dp = []
    times_greedy = []
    times_gpu = []
    times_brute = []
    for scale in scales:
        tm1 = 0
        tm2 = 0
        tm3 = 0
        tm4 = 0
        for i in range(1):
            start_time = time.time()
            dynamic.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm1 += end_time - start_time
            
            start_time = time.time()
            greedy.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm2 += end_time - start_time

            start_time = time.time()
            gpu.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm3 += end_time - start_time

            start_time = time.time()
            bruteforce.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm4 += end_time - start_time

            
        times_dp.append(tm1/5)
        times_greedy.append(tm2/5)
        times_gpu.append(tm3/5)
        times_brute.append(tm4/5)

    return times_dp, times_greedy, times_gpu, times_brute

def plot_runtime_vs_scaleb(scales, times_dp, times_greedy, times_gpu, times_brute):
    plt.figure(figsize=(10, 6))
    plt.plot(scales, times_dp, label='Dynamic Programming')
    plt.plot(scales, times_greedy, label='Greedy')
    plt.plot(scales, times_gpu, label='GPU')
    plt.plot(scales, times_brute, label='Bruteforce')
    plt.title('Runtime Comparison of Algorithms for the Image at Different Scales')
    plt.xlabel('Scale')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function to plot the runtime of algorithms for the image at different scales
def plot_runtime_vs_scale(scales, times_dp, times_greedy, times_gpu):
    plt.figure(figsize=(10, 6))
    plt.plot(scales, times_dp, label='Dynamic Programming')
    plt.plot(scales, times_greedy, label='Greedy')
    plt.plot(scales, times_gpu, label='GPU')
    plt.title('Runtime Comparison of Algorithms for the Image at Different Scales')
    plt.xlabel('Scale')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_onealg(lab):
    times = []
    for scale in scales:
        tm = 0
        for i in range(5):
            start_time = time.time()
            if lab == "dynamic":
                dynamic.main2('c', 1-scale, image_path, 'output.jpg')
            elif lab == "greedy":
                greedy.main2('c', 1-scale, image_path, 'output.jpg')
            elif lab == "bruteforce":
                bruteforce.main2('c', 1-scale, image_path, 'output.jpg')
            else:
                gpu.main2('c', 1-scale, image_path, 'output.jpg')
            end_time = time.time()
            tm += end_time - start_time
        times.append(tm/5)

    plt.plot(scales, times, label=lab)
    plt.title(f'Runtime of {lab} for the Image at Different Scales')
    plt.xlabel('Scale')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()


# Main function
if __name__ == '__main__':
    scales = [0, 0.1, 0.3, 0.5, 0.7]  # Add more scales as needed
    times_dp, times_greedy, times_gpu = time_algorithms(scales)
    plot_runtime_vs_scale(scales, times_dp, times_greedy, times_gpu)

    # times_dp, times_greedy, times_gpu, times_brute = time_algorithms_b(scales)
    # plot_runtime_vs_scaleb(scales, times_dp, times_greedy, times_gpu, times_brute)
    # plot_onealg("greedy")
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