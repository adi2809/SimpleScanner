## SimpleScanner
this is the submission to the assignment one of JRL302-Robotics-Technology at Indian Institute of Technology Delhi for the semester one 2021-2022

**project dependencies** : 
python, open-cv, numpy, argparse.

**brief description of programme files** :

1) **input_output.py** - written for implementing the reading of images, text files from specified path.
2) **compute_homography.py** - written for implementing the computation of perspective transform from source coordinates to destination coordinates.
3) **post_processing.py** - written for implementing histogram equalisation/ whitebalance for the image (added functionality not integrated in main)
4) **main.py** - written to run the app using a simple terminal call which will be explained in the instructions below for running the programme.


**logic flow behind the implementation** :

  -the method is based on the idea suggested in this mathematics stack-exchange post ( https://math.stackexchange.com/a/1289595/613549 ).

the basic idea of the implementation lies in how to solve the linear system of equations to find the 8-unknown paramters of the projective matrix namely h11, h12, h13, h21, h22, h23, h31, h32 ( we can take h33 = 1). 


**instructions for running the programme in the terminal** :

*python/ python3 main.py --image [path of image file] --coords [path of coordinates file in form of a .txt]*

  - image file can be a .png, .jpg or other formats that can be read by the opencv-python library's imread()
  - in the coords.txt file the following format is to be followed: 
    - top_left_x,top_left_y
    - top_right_x,top_right_y
    - btm_right_x,btm_right_y
    - btm_left_x,btm_left_y

  - **files in the test_images folder** : 
    - test_0.png, the image on which we tested the programme.
  - **files in the test_coords folder** : 
    - coords_0.txt the coordinates of the four points for the perspective transform in the order specified above for the test_0.img.


right now we need to manually determine the four points (using GIMP v 2.0) but work can be further improved by :
1) using a GUI - based drag service for the user (implement using tkinter).
2) using opencv - based automatic detection of the countour and the largest feasible rectangle.
