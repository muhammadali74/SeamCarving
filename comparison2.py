
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
# image_path = "random_image.jpg"


# Function to time the execution of each algorithm on the image
def time_algorithms(paths):
    scale = 0.5
    times_dp = []
    times_greedy = []
    times_gpu = []
    times_brute = []
    for image_path in paths:
        tm1 = 0
        tm2 = 0
        tm3 = 0
        for i in range(1):
            start_time = time.time()
            dynamic.main2('c', scale, image_path, 'output.jpg')
            end_time = time.time()
            tm1 += end_time - start_time
            
            start_time = time.time()
            greedy.main2('c', scale, image_path, 'output.jpg')
            end_time = time.time()
            tm2 += end_time - start_time

            start_time = time.time()
            gpu.main2('c', scale, image_path, 'output.jpg')
            end_time = time.time()
            tm3 += end_time - start_time
        times_dp.append(tm1/5)
        times_greedy.append(tm2/5)
        times_gpu.append(tm3/5)

    return times_dp, times_greedy, times_gpu

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
    scale  = 0.5
    for image_path in img_paths:
        tm = 0
        for i in range(5):
            start_time = time.time()
            if lab == "dynamic":
                dynamic.main2('c', scale, image_path, 'output.jpg')
            elif lab == "greedy":
                greedy.main2('c', scale, image_path, 'output.jpg')
            elif lab == "bruteforce":
                bruteforce.main2('c', scale, image_path, 'output.jpg')
            else:
                gpu.main2('c', scale, image_path, 'output.jpg')
            end_time = time.time()
            tm += end_time - start_time
        times.append(tm/5)

    plt.plot(dims, times, label=lab)
    plt.title(f'Runtime of {lab} for the Image at Different Scales')
    plt.xlabel('Scale')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()

img_paths = ["img4.jpg", "img3.jpg", "img2.jpg", "imgg1.jpg", "img5.jpg"]

dims = [180, 360, 480, 720, 1080]
# Main function
if __name__ == '__main__':
    times_dp, times_greedy, times_gpu = time_algorithms(img_paths)
    plot_runtime_vs_scale(dims, times_dp, times_greedy, times_gpu)
    # plot_onealg("greedy")

