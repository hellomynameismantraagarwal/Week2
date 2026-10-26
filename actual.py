import cv2
import numpy as np

#Reading
def tsk2(source, fl = 0.5):
    image = cv2.imread(source)
    image = cv2.resize(image, (1000,700))
    cv2.imshow("Original", image)

    #Converting to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

    #Masking yello and white
    lyello = np.array([15, 70, 220])
    hyello = np.array([40, 255, 255])
    lwhite = np.array([0, 0, 180])
    hwhite = np.array([180, 60, 255])

    wmask = cv2.inRange(hsv, lwhite, hwhite)
    ymask = cv2.inRange(hsv, lyello, hyello)

    mask = cv2.bitwise_or(ymask, wmask)

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Gaussian Blur
    bl = cv2.GaussianBlur(mask, (5,5), 0)
    _, thresh = cv2.threshold(grey, 170, 255, cv2.THRESH_BINARY)

    #countour
    # countours, hi = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(image, countours, contourIdx=-1, color=(0,255,0), thickness= 3)

    #Canny Edges
    cann = cv2.Canny(bl, 50,150) #only white or yellow

    #Const. ROI
    height, width = cann.shape

    roi_mask = np.zeros_like(cann)
    roi_mask2 = np.zeros_like(cann)

    polygon = np.array([[
        (int(width * 0.02), height*fl), #Bottom Left
        (int(width * 0.98), height*fl), #Bottom right
        (int(width * 0.55), int(height*0.25)), #Top-right
        (int(width * 0.45), int(height*0.25)) #Top left
    ]], dtype=np.int32)

    polygon2 = np.array([[
        (int(width * 0.02), height-1), #Bottom Left
        (int(width * 0.98), height-1), #Bottom right
        (int(width * 0.98), int(height*fl)), #Top-right
        (int(width * 0.02), int(height*fl)) #Top left
    ]], dtype=np.int32)

    cv2.fillPoly(roi_mask, polygon, 255)

    cv2.fillPoly(roi_mask2, polygon2, 255)

    # roi_mask3 = cv2.bitwise_or(roi_mask2, roi_mask)

    roi_edges = cv2.bitwise_and(cann, roi_mask2)

    con, hii = cv2.findContours(roi_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, con, contourIdx=-1, color = (0,255,255), thickness= 3)

    
    #Showing images
    cv2.imshow("HSV", hsv)
    # cv2.imshow("Gaussian Blur", bl)
    # cv2.imshow("cann", cann)
    cv2.imshow("Final Lane Edges", roi_edges)
    cv2.imshow("original with contours", image)
    #End
    # cv2.imshow("MSK", mask)
    # cv2.imshow("roi2 mask", roi_mask2)
    print(con)
    for cont in con:
        print(cont, len(cont))





    cv2.waitKey(0)
    cv2.destroyAllWindows()
tsk2('/home/mantra/Desktop/Workstuff/CEAM CV/Week2/poto3.png', 0.7)
tsk2('/home/mantra/Desktop/Workstuff/CEAM CV/Week2/images.jpeg', 0.4)
# tsk2('/home/mantra/Desktop/Workstuff/CEAM CV/Week2/poto.png', 0.3)