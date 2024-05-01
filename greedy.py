#!/usr/bin/env python

"""
Usage: python carver.py <r/c> <scale> <image_in> <image_out>
Copyright 2018 Karthik Karanth, MIT License
"""

import sys

from tqdm import trange
import numpy as np
from imageio.v2 import imread, imwrite
from scipy.ndimage import convolve



def calc_energy(img):
    filter_du = np.array([
        [1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0],
        [-1.0, -2.0, -1.0],
    ])
    # This converts it from a 2D filter to a 3D filter, replicating the same
    # filter for each channel: R, G, B
    filter_du = np.stack([filter_du] * 3, axis=2)

    filter_dv = np.array([
        [1.0, 0.0, -1.0],
        [2.0, 0.0, -2.0],
        [1.0, 0.0, -1.0],
    ])
    # This converts it from a 2D filter to a 3D filter, replicating the same
    # filter for each channel: R, G, B
    filter_dv = np.stack([filter_dv] * 3, axis=2)

    img = img.astype('float32')
    convolved = np.absolute(convolve(img, filter_du)) + np.absolute(convolve(img, filter_dv))

    # We sum the energies in the red, green, and blue channels
    energy_map = convolved.sum(axis=2)

    return energy_map

def crop_c(img, scale_c):
    r, c, _ = img.shape
    new_c = int(scale_c * c)

    for i in trange(c - new_c):
        img = carve_column(img)

    return img

def crop_r(img, scale_r):
    img = np.rot90(img, 1, (0, 1))
    img = crop_c(img, scale_r)
    img = np.rot90(img, 3, (0, 1))
    return img


def carve_column(img):
    r, c, _ = img.shape

    indices = greedy_seam(img)
    mask = np.ones((r, c), dtype=bool)

    for i in range(len(indices)):
        mask[i, indices[i]] = False

    mask = np.stack([mask] * 3, axis=2)
    img = img[mask].reshape((r, c - 1, 3))
    # print("column carved")
    return img


def greedy_seam(img):
    r, c, _ = img.shape
    energy_map = calc_energy(img)

    M = energy_map.copy()
    
    min_start = np.argmin(M[0])
    seam_indixes = []
    seam_indixes.append(min_start)

    for i in range(1, r):
        if min_start == 0:
            offset = np.argmin(M[i, min_start:min_start + 2])
            min_start += offset
            seam_indixes.append(min_start + offset)
            
        else:
            offset = np.argmin(M[i, min_start - 1:min_start + 2])
            min_start = min_start + offset -1
            seam_indixes.append(min_start)

    # print(seam_indixes)
    return seam_indixes

def main2(axis, scale, inp, output):
    img = imread(inp)

    if axis == 'r':
        out = crop_r(img, scale)
    elif axis == 'c':
        out = crop_c(img, scale)
    else:
        print('usage: carver.py <r/c> <scale> <image_in> <image_out>', file=sys.stderr)
        sys.exit(1)
    
    imwrite(output, out)

'''
def main():
    if len(sys.argv) != 5:
        print('usage: carver.py <r/c> <scale> <image_in> <image_out>', file=sys.stderr)
        sys.exit(1)

    which_axis = sys.argv[1]
    scale = float(sys.argv[2])
    in_filename = sys.argv[3]
    out_filename = sys.argv[4]

    img = imread(in_filename)

    if which_axis == 'r':
        out = crop_r(img, scale)
    elif which_axis == 'c':
        out = crop_c(img, scale)
    else:
        print('usage: carver.py <r/c> <scale> <image_in> <image_out>', file=sys.stderr)
        sys.exit(1)
    
    imwrite(out_filename, out)

if __name__ == '__main__':
    main()
    '''