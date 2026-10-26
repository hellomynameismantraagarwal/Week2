So I have used OpenCV here, by import cv2 As we have to use computer vision to do so.


 IMAGE READING:
|->so first I have used cv.imread() to read the given image and store it in a variable image then resized it by cv2.resize()
 
 CONVERTING TO HSV cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
|->Then I assigned a new variable hsv to and assigned the HSV varient of the original image as per the instructions for robust color and filtering
|->I also made two ranges for yellow and white colour as a for a road detection majorly yello and white lines are created, So my thought process was to detect the lines from the image and then would create a polygon and use a binary operation (cv2.bitwise_and) to get the yellow/white lines. I assigned it in a variable mask

 GReYSCALing: grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
|-> I created a new variable grey and assinged the grayscale image to it as it will be required for contours.

 GAUSSIAN BLUR: bl = cv2.GaussianBlur(mask, (5,5), 0)
|->Similarly I created a new variable assigned the blurred image of the mask
|->Kernel size is 5x5

 THRESHOLDING: _, thresh = cv2.threshold(grey, 170, 255, cv2.THRESH_BINARY)
|-> For contour drawing thresholding is necessary

 CONTOURS:
|-> Finding contours on thresh
|-> Drew contours on the original image

 CANNY EDGES:
|-> Assigned new variable cann for canny edges from the bl
|-> Used range (50,150)-> Was handpicked by me after some hit and trials

 ROI:
|-> Created an empty matrix with an estimated road of fully white colour
|-> Created a polygon which is fully white, created through numpy matrix, had to create another polygon for accurate polygon shape, then joined them via binary operation (cv2.bitwise_or)
|-> The values were again handpicked by me after a lot of hit and trials
|-> Then I used cv2.bitwise_and(roi_mask3, cann) getting only the common things between polygon and the cann basically just got the common image of the polygon and the part of the road which is yellow or white coloured



