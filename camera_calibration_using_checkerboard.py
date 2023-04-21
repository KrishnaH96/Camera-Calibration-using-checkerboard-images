import numpy as np
import cv2 as cv
import os

# termination criteria
check_criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 50, 0.003)

real = []
for i in range(6):
    for j in range(9):
        real.append([j, i, 0])
real = np.array(real, dtype=np.float32) * 21.5

real_points = [] 
image_points = [] 

path_to_images = "C:/Masters/Spring 2023/ENPM673_Perception/Perception/Project 3/Submission/krishnah_proj3/Problem2/images"
standard_chessboards = [os.path.join(path_to_images, f) for f in os.listdir(path_to_images) if f.endswith('.jpg')]


for i, image_file in enumerate(standard_chessboards):
    img = cv.imread(image_file)
    scaling_factor = 1

    w=int(img.shape[1]* scaling_factor)
    h=int(img.shape[0]* scaling_factor)
    img = cv.resize(img, (w,h))
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

    ret, corners = cv.findChessboardCorners(gray, (9,6), None)

    if ret == True:
        real_points.append(real)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), check_criteria)
        image_points.append(corners2)

        for corner in corners2:
            x, y = tuple(map(int, corner.ravel()))
            cv.circle(img, (x, y), 15, (255 , 0, 255), -1)
        
        cv.namedWindow('Resized Window', cv.WINDOW_NORMAL)
        cv.resizeWindow('Resized Window', int(w* 0.6), int(h * 0.6))
        cv.imshow('Resized Window', img)
        # cv.imwrite(f'Chessboard_with_corners{i+1}.jpg', img)
        cv.waitKey(500)

    else:   
        print('Error: Chessboard corners not found in image', image_file)

cv.destroyAllWindows()

ret, camera_intrinsic_matrix, dist, rotation_matrix, tvecs = cv.calibrateCamera(real_points, image_points, gray.shape[::-1], None, None)

# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~: \n")
print("The camera intrinsic matrix (K): \n")
print(camera_intrinsic_matrix)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~: \n")

total_error = 0
for i in range(len(real_points)):
    imgpoints2, _ = cv.projectPoints(real_points[i], rotation_matrix[i], tvecs[i], camera_intrinsic_matrix, dist)
    error = cv.norm(image_points[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~: \n")
    print(f" The reprojection error for {i+1}th image is {error}.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~: \n")
    total_error += error

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~: \n")
print( "Mean error: {} \n".format(total_error/len(real_points)))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~: \n")
