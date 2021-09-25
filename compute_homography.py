import numpy as np 

def compute_homography(src, dst):

    """computes the homography from src, to dst using inversion method."""
    
    if src.shape[1] == 2 :
        p1 = np.ones((len(src),3),'float64')
        p1[:,:2] = src
    elif src.shape[1] == 3 : p1 = src
    
    
    if dst.shape[1] == 2 :
        p2 = np.ones((len(dst),3),'float64')
        p2[:,:2] = dst
    elif dst.shape[1] == 3 : p2 = dst
    
    
    npoints = len(src)
    count = 2*npoints +1
    A = np.zeros((count,9),'float32')
    
    #populating the matrix A 
    
    for i in range(npoints):
        p1i = p1[i]
        x2i,y2i,w2i = p2[i]
        xpi = x2i*p1i
        ypi = y2i*p1i
        wpi = w2i*p1i
        
        A[i*2+1,3:6] = -wpi
        A[i*2+1,6:9] =  ypi
        A[i*2  ,0:3] = -wpi
        A[i*2  ,6:9] =  xpi
        

    A[8,8] = 1
    B = np.zeros((9,1))
    B[8,0] = 1
    h = (np.linalg.inv(A))@B
    print(np.linalg.inv(A).shape)

    H = h.reshape(3,3)
    return H

def find_homography(src,dst):
	"""computes the homography from src, to dst using singular value decomposition method."""
	
	if src.shape[1] == 2 :
		p1 = np.ones((len(src),3),'float64')
		p1[:,:2] = src
	elif src.shape[1] == 3 : p1 = src
	
	
	if dst.shape[1] == 2 :
		p2 = np.ones((len(dst),3),'float64')
		p2[:,:2] = dst
	elif dst.shape[1] == 3 : p2 = dst
	
	
	npoints = len(src)
	count = 3*npoints
	A = np.zeros((count,9),'float32')
	
    #populating the matrix A (TO BE DECOMPOSED).
    #least squares fitting algorithm/ SVD algorithm.
	for i in range(npoints):
		p1i = p1[i]
		x2i,y2i,w2i = p2[i]
		xpi = x2i*p1i
		ypi = y2i*p1i
		wpi = w2i*p1i
		
		A[i*3  ,3:6] = -wpi
		A[i*3  ,6:9] =  ypi
		A[i*3+1,0:3] =  wpi
		A[i*3+1,6:9] = -xpi
		A[i*3+2,0:3] = -ypi
		A[i*3+2,3:6] =  xpi

	U,s,V = np.linalg.svd(A)

    #we need the last set of non-singular values only 
	h = V[-1]
	H = h.reshape(3,3)
	return H


def find_homography_2(src,dst):
    """computes the homography from src, to dst using singular value decomposition method."""
    
    if src.shape[1] == 2 :
        p1 = np.ones((len(src),3),'float64')
        p1[:,:2] = src
    elif src.shape[1] == 3 : p1 = src
    
    
    if dst.shape[1] == 2 :
        p2 = np.ones((len(dst),3),'float64')
        p2[:,:2] = dst
    elif dst.shape[1] == 3 : p2 = dst
    
    
    npoints = len(src)
    count = 2*npoints +1
    A = np.zeros((count,9),'float32')
    
    #populating the matrix A (TO BE DECOMPOSED).
    #least squares fitting algorithm/ SVD algorithm.
    for i in range(npoints):
        p1i = p1[i]
        x2i,y2i,w2i = p2[i]
        xpi = x2i*p1i
        ypi = y2i*p1i
        wpi = w2i*p1i
        
        A[i*2+1,3:6] = -wpi
        A[i*2+1,6:9] =  ypi
        A[i*2  ,0:3] = -wpi
        A[i*2  ,6:9] =  xpi
        
    U,s,V = np.linalg.svd(A)

    #we need the last set of non-singular values only 
    h = V[-1]
    H = h.reshape(3,3)
    return H

