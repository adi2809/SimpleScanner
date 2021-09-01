import cv2
import numpy as np
from input_output import read_image

def histogram_equalisation(srcpath, dstpath):
    """histogram equalisation using open-cv"""
    img = read_image(srcpath)

    new_img = cv2.equalizeHist(img)
    cv2.imwrite(dstpath)

    return None

