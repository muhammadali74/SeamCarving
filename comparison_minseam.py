# import packages
import time
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
from PIL import Image
import numpy as np

# import files 
from seamcarving import minimum_seam
from greedy import greedy_seam
from dynamic_gpu import minimum_seam as gpu_seam
from bruteforce import brute_seam

def time_minimum_seams(paths):
    times_dp = []
    times_greedy = []
    times_gpu = []
    for image_path in paths:
        avg_time_dp = 0
        avg_time_greedy = 0
        avg_time_gpu = 0
        for _ in range(0, 5):
            image = imread(image_path) 
            start_time = time.time()
            minimum_seam(image)
            end_time = time.time()
            avg_time_dp += end_time - start_time
            
            start_time = time.time()
            greedy_seam(image)
            end_time = time.time()
            avg_time_greedy += end_time - start_time

            start_time = time.time()
            gpu_seam(image)
            end_time = time.time()
            avg_time_gpu += end_time - start_time

        print("Average time of Dynamic Programming Seam: ", avg_time_dp / 5)
        print("Average time of Greedy Algorithm Seam: ", avg_time_greedy / 5)
        print("Average time of GPU Seam: ", avg_time_gpu / 5, "\n")

        times_dp.append(avg_time_dp / 5)
        times_greedy.append(avg_time_greedy / 5)
        times_gpu.append(avg_time_gpu / 5)

    return times_dp, times_greedy, times_gpu


def image_generator():
    # image size
    sizes = [5, 10, 15, 20]
    img_paths = []

    # generates images
    for size in sizes:
        random_image = np.random.randint(0, 256, (size, size, 3), dtype=np.uint8)
        random_image = Image.fromarray(random_image, 'RGB')

        random_image.save(f'random_image_{size}x{size}.jpg')
        img_paths.append(f'random_image_{size}x{size}.jpg')

    return img_paths


# brute force is implemented separately due to its time complexity 
def time_bf_seam(paths):
    times_bruteforce = []
    for image_path in paths:
        avg_time_bruteforce = 0 
        for _ in range(0, 5):
            image = imread(image_path) 
            start_time = time.time()
            brute_seam(image)  
            end_time = time.time()
            avg_time_bruteforce += end_time - start_time

        times_bruteforce.append(avg_time_bruteforce / 5)
        print("Average time of Brute Force Seam: ", avg_time_bruteforce / 5)

    return times_bruteforce


# Function to plot the runtime of minimum seam functions for the image
def plot_runtimes_all(scales, times_dp, times_greedy, times_bruteforce, times_gpu):
    plt.figure(figsize=(10, 6))
    plt.plot(scales, times_dp, label='Dynamic Programming')
    plt.plot(scales, times_greedy, label='Greedy')
    plt.plot(scales, times_bruteforce, label='Brute Force')
    plt.plot(scales, times_gpu, label='GPU Parallelization')
    plt.title('Runtime Comparison of Minimum Seam Functions for the Image')
    plt.xlabel('Image Index')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Function to plot the runtime of a single algorithm for the image
def plot_individual_methods(label, dims, time_array):
    plt.figure(figsize=(10, 6))
    plt.plot(dims, time_array, label=label)
    plt.title(f'Runtime of {label} for the Image at Different Scales')
    plt.xlabel('Scale')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()


bf_images = image_generator()
img_paths = ["img4.jpg", "img3.jpg", "img2.jpg", "imgg1.jpg", "img5.jpg"]

# Main function
if __name__ == '__main__':
    times_dp, times_greedy, times_gpu = time_minimum_seams(img_paths)
    times_bruteforce = time_bf_seam(bf_images)
    scales = np.arange(len(img_paths))
    plot_runtimes_all(scales, times_dp, times_greedy, times_bruteforce, times_gpu)
    plot_individual_methods("Dynamic Programming Seam Carving", scales, times_dp)
    plot_individual_methods("Greedy Approach Seam Carving", scales, times_greedy)
    plot_individual_methods("Bruteforce Seam Carving", scales, times_bruteforce)
    plot_individual_methods("GPU Parallelization", scales, times_gpu)
