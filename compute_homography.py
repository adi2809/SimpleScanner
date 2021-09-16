import numpy as np 

#def compute_homography(src, dst):
     """linear equation solver, did not pan out great and we had to write a lot manually.
         so did not use this approach as it was bulky."""
	
	x_1 = src[0]
	y_1 = dst[0]
	x_2 = src[1]
	y_2 = dst[1]
	x_3 = src[2]
	y_3 = dst[2]
	x_4 = src[3]
	y_4 = dst[3]
	P = np.array([
		[-x_1[0], -y_1[0], -1, 0, 0, 0, x_1[0]*x_1[1], y_1[0]*x_1[1], x_1[1]],
		[0, 0, 0, -x_1[0], -y_1[0], -1, x_1[0]*y_1[1], y_1[0]*y_1[1], y_1[1]],
		[-x_2[0], -y_2[0], -1, 0, 0, 0, x_2[0]*x_2[1], y_2[0]*x_2[1], x_2[1]],
		[0, 0, 0, -x_2[0], -y_2[0], -1, x_2[0]*y_2[1], y_2[0]*y_2[1], y_2[1]],
		[-x_3[0], -y_3[0], -1, 0, 0, 0, x_3[0]*x_3[1], y_3[0]*x_3[1], x_3[1]],
		[0, 0, 0, -x_3[0], -y_3[0], -1, x_3[0]*y_3[1], y_3[0]*y_3[1], y_3[1]],
		[-x_4[0], -y_4[0], -1, 0, 0, 0, x_4[0]*x_4[1], y_4[0]*x_4[1], x_4[1]],
		[0, 0, 0, -x_4[0], -y_4[0], -1, x_4[0]*y_4[1], y_4[0]*y_4[1], y_4[1]],
		[0, 0, 0, 0, 0, 0, 0, 0, 1]])
	
    

	b = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1]).reshape((9,1))

    homography = (np.linalg.pinv(A) @ b).reshape((3,3))
    

    
    
    return homography

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




