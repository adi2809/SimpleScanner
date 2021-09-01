import os
import cv2
import math
import argparse
import numpy as np 
from input_output import *
from post_processing import *
from compute_homography import *

def main(args):
    #read the image (input)
    img = read_image(args.image)
    #formulate the src and dest. coordinates.
    #points are read from a ASCII text file. 
    #order of points is : 
    #1) top left, 2) top_right, 3)bottom_right, 4) bottom_left
    src = read_coords(args.coords)
    dst = generate_destination(src)


    #dealing with the scale factor : find the final image sizes. use max width 
    #use max height 
    top_left, top_right, btm_right, btm_left = src[0], src[1], src[2], src[3]
    
    w1, w2 = np.linalg.norm(btm_right-btm_left), np.linalg.norm(top_right-top_left)
    w_max = max(ceil(w1), ceil(w2))

    h1, h2 = np.linalg.norm(top_right-btm_right), np.linalg.norm(top_left-btm_right)
    h_max = max(ceil(h1), ceil(h2))

    #compute the homography using linear equation solving using singular value decomp. 
    H = find_homography(src, dst)
    print(H) #prints the matrix computed using our method (note it is general matrix none of hij may be one)

    #use the open-cv routine to warp the image using the obtained matrix. 
    new_img = cv2.warpPerspective(img, H, (w_max, h_max))

    #save the final image onto the current directory with the name result.png.
    cv2.imwrite('result.png', new_img)
    print("SUCCESSFUL!")
    return None

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image', help='path to src image'
    )
    parser.add_argument(
        '--coords',
        help=' path to list of coordinates'
    )

    args = parser.parse_args()
    main(args)



    

    