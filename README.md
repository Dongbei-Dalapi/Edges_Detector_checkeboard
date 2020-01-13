# Edges Detector on checkerboard
The goal of this project is to detect the edges in a checkerboard and highlight them with a green line superimposed on the image.
## 1.1 Used tools
The project has been developed using Python and open source libraries. In particular it's been used:
* Python 3.7.3
* OpenCV 
* Numpy 
* Argparse 

## 1.2 Data
The *Data* folder include five pictures of chessboard. Each of them has different degree of noise and rotation.
![Figure_1](https://user-images.githubusercontent.com/38732983/72232658-cf88d480-35c2-11ea-9857-ba8e749ada43.png)

# 2 Implementation 
## 2.1 Noise Reduction
Since the mathematics involved behind the edge detection are mainly based on derivatives, the results are highly sensitive to image noise. One way to remov the noise on the image, is by applying filter to smooth it. To do so, image convolution technique can be applied with different Kernel. 
There are four common filters for noise removal:
1. Averaging 
2. Gaussian 
3. Median 
4. Bilateral

## 2.2 Threshold
Threshold is used to detect the edges more clearly when the checkerboard is not a black and white picture. 

## 2.3 edges detection
Edges detection aims to find the boundaries of objects within images.

# 3 Run the Project
## 3.1 Installation
In order to run the python file, the following packages must be installed.
```
# pip 
sudo easy_install pip
   
# OpenCV (cv2)
pip install opencv-python

# Numpy
pip install numpy

# Argparse 
pip install argparse
```
## 3.2 Run the Program
Launch the python edge_detector.py with the parameters `input` [input filename]
cd {project_folder}







