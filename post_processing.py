import cv2
import numpy as np
from input_output import read_image

def histogram_equalisation(srcpath, dstpath):
    """histogram equalisation using open-cv"""
    img = read_image(srcpath)

    new_img = cv2.equalizeHist(img)
    cv2.imwrite(dstpath)

    return None

def histogram_equalisationFromScratch(img): 
    """
    this function implements the eaualisation algorithm for 
    an image from scratch. does not use open-cv for the op. 
    """
    
    def get_histogram(img):
        """
        find the histogram
        for the given image
        """
        m, n = img.shape #dimensions of the digital image.
        h = [0.0] * 256 #initiating the histogram for intensities of the pixel from 0-255
        
        for i in range(m):
            for j in range(n):
                h[img[i, j]]+=1
        
        return np.array(h)/(m*n)

    def cumsum(h):
        """finds cumulative sum of a numpy array, list"""
        return [sum(h[:i+1]) for i in range(len(h))]

    def histeq(img):
        #calculate Histogram
        h = get_histogram(img)
        cdf = np.array(cumsum(h)) #cumulative distribution function
        sk = np.uint8(255 * cdf) #finding transfer function values

        m, n = img.shape
        Y = np.zeros_like(img)

        # applying transfered values for each pixels
        for i in range(0, m):
            for j in range(0, n):
                Y[i, j] = sk[img[i, j]]
        
        H = get_histogram(Y)
    
        #return transformed image, original and new istogram, 
        # and transform function
        return Y, h, H, sk
    
    return histeq(img)

