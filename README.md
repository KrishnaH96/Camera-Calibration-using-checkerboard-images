# Camera Calibration using OpenCV

This program is used to calibrate a camera using OpenCV library in Python. The camera calibration is the process of determining the intrinsic and extrinsic parameters of a camera, which are necessary to correctly map 3D points in the world to their corresponding 2D image points.

## Required Libraries
This program requires the following libraries to be installed:
- numpy
- cv2 (OpenCV)
- os

## Code Flow
1. The program first imports the required modules i.e. numpy, cv2 and os.
2. The termination criteria for iterative algorithms used in OpenCV are defined based on the number of iterations or accuracy. Here, after some iterations, the termination criteria are set with 50 iterations and accuracy of 0.003.
3. The program defines the coordinates of the chessboard corners in the real world space. The points are arranged in a grid of 6 x 9 with z=0, with a grid size of 21.6mm.
4. Two lists are created, real_points and image_points, to store the object points and image points respectively. The object points represent the 3D coordinates of the corners in the real world space, while the image points represent their corresponding 2D coordinates in the image plane.
5. The path to the folder containing calibration images is set in the variable path_to_images, and the list of all the image files with extension '.jpg' from the path_to_images folder is obtained and stored in the standard_chessboards list.
6. The program loops through all the images in the standard_chessboards list:
    - Reads the image using cv2.imread() method.
    - Resizes the image using cv2.resize() method with scaling_factor = 1.
    - Converts the image from BGR to grayscale using cv2.cvtColor() method.
    - Finds the chessboard corners using cv2.findChessboardCorners() method.
    - If the corners are found in the image, then refines the corners using cv2.cornerSubPix() method.
    - Adds the refined corners (image points) and the real object points to the respective lists (image_points and real_points).
    - Draws circles at the refined corner points on the image using cv2.circle() method.
    - Displays the image with refined corner points using cv2.imshow() method and waits for 500 milliseconds before moving to the next image.
    - If the corners are not found in the image, then prints an error message.
7. The camera is calibrated using cv2.calibrateCamera() method with the real_points and image_points.
8. The intrinsic camera matrix (K) is printed.
9. The program loops through all the images in the real_points list and calculates the reprojection error using cv2.projectPoints() method.
    - Calculates the L2 norm of the difference between the image_points and imgpoints2 using cv2.norm() method and divides it by the length of imgpoints2 to get the average error.
    - Adds the error to the total_error variable.
10. The mean error and the error matrix are printed using the print() method.

## Installation

To run the code in this repository, you need to have the following packages installed:

- OpenCV
- NumPy
- OS

You can install the required packages using pip:

```
pip install opencv-python numpy
```
## Usage

To use this code, follow these steps:

1. Clone this repository: `https://github.com/KrishnaH96/Camera-Calibration-using-checkerboard-images.git`
2. provide the path of the folder where the thriteen images of the checkerboard are saved. (These Images are available in the git repository).
3. Run the Python script.
4. The program will display Intrinsic Matrix of the camera, all thirteen images with feature points highlighted and mean reprojection error.

## Contributing

If you find any issues with the code or want to suggest improvements, feel free to open an issue or create a pull request in this repository. 

## Conclusion
In conclusion, this program can be used to calibrate a camera using OpenCV in Python. It is a very useful tool for computer vision applications such as object detection, tracking, and 3D reconstruction.

I added the report i submitted for the problem in the repository as well for reference.

