# import packages
import time
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread


# import files 
from seamcarving import minimum_seam
from greedy import greedy_seam
from dynamic_gpu import minimum_seam as gpu_seam

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


# Function to plot the runtime of minimum seam functions for the image
def plot_runtime_vs_scale(scales, times_seamcarving, times_greedy, times_gpu):
    plt.figure(figsize=(10, 6))
    plt.plot(scales, times_seamcarving, label='Dynamic Programming')
    plt.plot(scales, times_greedy, label='Greedy')
    plt.plot(scales, times_gpu, label='GPU Parallelization')
    plt.title('Runtime Comparison of Minimum Seam Functions for the Image')
    plt.xlabel('Image Index')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.tight_layout()
    plt.show()


img_paths = ["img4.jpg", "img3.jpg", "img2.jpg", "imgg1.jpg", "img5.jpg"]

# Main function
if __name__ == '__main__':
    times_dp, times_greedy, times_gpu = time_minimum_seams(img_paths)
    plot_runtime_vs_scale(np.arange(len(img_paths)), times_dp, times_greedy, times_gpu)