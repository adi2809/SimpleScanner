import cv2 
from math import ceil
import numpy as np 

def read_image(path):
    mat = cv2.imread(path)
    return mat 


def read_coords(path):
    coords = []
    with open(path) as f: 
        for line in f:
            x, y = line.split(",")
            coords.append([x, y])
    return np.float32(np.array(coords))


def save_image(img, path):
    cv2.imwrite(img, path)
    return None

def generate_destination(coords):
    top_left, top_right, btm_right, btm_left = coords[0], coords[1], coords[2], coords[3]
    
    w1, w2 = np.linalg.norm(btm_right-btm_left), np.linalg.norm(top_right-top_left)
    w_max = max(ceil(w1), ceil(w2))

    h1, h2 = np.linalg.norm(top_right-btm_right), np.linalg.norm(top_left-btm_right)
    h_max = max(ceil(h1), ceil(h2))

    dst = np.array([[0, 0],[w_max-1, 0],[w_max-1, h_max-1], [0, h_max-1]])

    return np.float32(dst)