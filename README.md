# SimpleScanner
this is the submission to the assignment one of JRL302-Robotics-Technology at Indian Institute of Technology Delhi for the semester one 2021-2022

project dependencies : 
python, open-cv, numpy, argparse.

breif description of programme files :

1) input_output.py - written for implementing the reading of images, text files from specified path.
2) compute_homography.py - written for implementing the computation of perspective transform from source coordinates to destination coordinates.
3) post_processing.py - written for implementing histogram equalisation/ whitebalance for the image (added functionality not integrated in main)
4) main.py - written to run the app using a simple terminal call which will be explained in the instructions below for running the programme .


logic flow behind the implementation :

the method is based on the idea suggested in this mathematics stack-exchange post (https://math.stackexchange.com/questions/494238/how-to-compute-homography-matrix-h-from-corresponding-points-2d-2d-planar-homog/2619023#2619023) 

the basic idea of the implementation lies in how to solve the linear system of equations to find the 8-unknown paramters of the projective matrix namely h11, h12, h13, h21, h22, h23, h31, h32 ( we can take h33 = 1). 

You can compute the homography matrix H with your eight points with a matrix system such that the four correspondance points $(p_1, p_1'), (p_2, p_2'), (p_3, p_3'), (p_4, p_4')$ are written as $2\times9$ matrices such as:

$p_i = \begin{bmatrix}
-x_i \quad -y_i \quad -1 \quad 0 \quad 0 \quad 0 \quad x_ix_i' \quad y_ix_i' \quad x_i' \\
0 \quad 0 \quad 0 \quad -x_i \quad -y_i \quad -1 \quad x_iy_i' \quad y_iy_i' \quad y_i'
\end{bmatrix}$

It is then possible to stack them into a matrix $P$ to compute:

$PH = 0$

Such as:

$PH = \begin{bmatrix}
-x_1 \quad -y_1 \quad -1 \quad 0 \quad 0 \quad 0 \quad x_1x_1' \quad y_1x_1' \quad x_1' \\
0 \quad 0 \quad 0 \quad -x_1 \quad -y_1 \quad -1 \quad x_1y_1' \quad y_1y_1' \quad y_1' \\
-x_2 \quad -y_2 \quad -1 \quad 0 \quad 0 \quad 0 \quad x_2x_2' \quad y_2x_2' \quad x_2' \\
0 \quad 0 \quad 0 \quad -x_2 \quad -y_2 \quad -1 \quad x_2y_2' \quad y_2y_2' \quad y_2' \\
-x_3 \quad -y_3 \quad -1 \quad 0 \quad 0 \quad 0 \quad x_3x_3' \quad y_3x_3' \quad x_3' \\
0 \quad 0 \quad 0 \quad -x_3 \quad -y_3 \quad -1 \quad x_3y_3' \quad y_3y_3' \quad y_3' \\
-x_4 \quad -y_4 \quad -1 \quad 0 \quad 0 \quad 0 \quad x_4x_4' \quad y_4x_4' \quad x_4' \\
0 \quad 0 \quad 0 \quad -x_4 \quad -y_4 \quad -1 \quad x_4y_4' \quad y_4y_4' \quad y_4' \\
\end{bmatrix} \begin{bmatrix}h1 \\ h2 \\ h3 \\ h4 \\ h5 \\ h6 \\ h7 \\ h8 \\h9 \end{bmatrix} = 0$

While adding an extra constraint $|H|=1$ to avoid the obvious solution of $H$ being all zeros. It is easy to use SVD $P = USV^\top$ and select the last singular vector of $V$ as the solution to $H$.

Note that this gives you a DLT (direct linear transform) homography that minimizes algebraic error. This error is not geometrically meaningful and so the computed homography may not be as good as you expect. One typically applies nonlinear least squares with a better cost function (e.g. symmetric transfer error) to improve the homography.

Once you have your homography matrix $H$, you can compute the projected coordinates of any point $p(x, y)$ such as:

$\begin{bmatrix}
  x' / \lambda \\
  y' / \lambda \\
  \lambda
 \end{bmatrix} =
\begin{bmatrix}
  h_{11} & h_{12} & h_{13} \\
  h_{21} & h_{22} & h_{23} \\
  h_{31} & h_{32} & h_{33}
 \end{bmatrix}.
\begin{bmatrix}
  x \\
  y \\
  1
 \end{bmatrix}$
 


instructions for running the programme in the terminal : type the following line with the necessary inputs on to the device's terminal. 

python/ python3 main.py --image [path of image file] --coords [path of coordinates file in form of a .txt]
- image file can be a .png, .jpg or other formats that can be read by the opencv-python library's imread().
- in the coords.txt file the following format is to be followed: 
  - top_left_x,top_left_y
  - top_right_x,top_right_y
  - btm_right_x,btm_right_y
  - btm_left_x,btm_left_y
