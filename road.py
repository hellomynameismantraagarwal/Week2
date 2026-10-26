import cv2

img = cv2.imread('roadwithcar.png')
image = cv2.imread("images.png")
cropped = img[10:30, 50:75]

(h, w) = img.shape[:2]
center = (w//2, h//2) #only getting the height and the width
M = cv2.getRotationMatrix2D(center, 90, 2.0) #parameters are center, degree, magnitude of zoom
rotated = cv2.warpAffine(img, M, (w,h))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV- Hue, saturation and value
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) #LAB- Lightness- Green-red(a), Blue-yellow(b) 

resized = cv2.resize(img, (1000,200)) #parameters are source, new dimension- (width, height), optional-(fx, fy, interpolation)

flipped = cv2.flip(img, 0) #flip(image, 1 for horizontal, 0 for vertical, -1 for both)

if img is None:
    print("Error")

else:

    # cv2.imshow("Rotated", rotated)
    # cv2.imshow("LAB", lab)
    # cv2.imshow("Resized", resized)
    cv2.imshow("HSV", hsv)
    # cv2.imshow("Flipped", flipped)

    #DRAWING:
    #Line
    # cv2.line(img, (50,100), (100,200), (255,0,0), 3)
    # cv2.rectangle(img, pt1 = (50,100), pt2 = (100,200), color=(12,25,200), thickness=-3)
    # cv2.circle(img, center=(150,150), radius=50, color=(0,40,150), thickness=-3) #negative values of thickness will fill it
    # cv2.putText(img, text="Hello", org=(150,100), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale=1.2, color = (100,100,100))
    # cv2.imshow("original image", img)
    #Gaussian Blur: cv2.GaussianBlur(image, (kernel_size_x, kernel_size_y)->Should always be odd number, sigma->How much magnitude of blurring), Kernel size also affects blurring, (3,3) for light, (7,7) for more and (21,21) for most blur
    blurred = cv2.GaussianBlur(img, (3,3), 1.3)
    cv2.imshow("Blurred" ,blurred)
    cv2.imshow("No", img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    #Threshold: cv2.threshold(image, threshold value, max value, cv2.THRESH_BINARY)
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    cv2.imshow("THRESHOLD", thresh)

    #Median Blur cv2.medianBlur(image, kernel_size)

    #Sharpening:   cv2.filter2D(source, ddepth-(-1), kernel)

    #Binary operations cv2.bitwise_and(img1, img2), cv2.bitwise_or(img1,img2), cv2.bitwise_nor(img)

    #Countours: countours, hierarchy = cv2.findCountours(image, mode-RETR_TREE, RETR_EXTERNAL, method-approx. method), mode takes how many counters to return and what kind of counters to return
    countours, hi = cv2.findContours(thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawCountours(image, countours, countour_index-0(first shape), 1(second shape), -1(All shape), color, thickness)
    cv2.drawContours(image, countours, -1, (0,255,0), 3)
    cv2.imshow("Contours", image)
    
    #Detecting shapes: approx = cv2.approxPolyDP(countour, epsilon, True->Indicates that it is a closed figure) epsilon is the border/parameter of the shape, epsilon = 0.01* cv2.arcLength(contour, True->Indicates that it is a closed figure), if smaller- more precise







    imgblur = cv2.GaussianBlur(image, (19,19), 1)
    #Image processing:
    #Canny Edge Detection- Detect borders| edges = cv2.Canny(image,threshold1,threshold2)
    edges = cv2.Canny(imgblur, 250, 255)
    cv2.imshow("Gray", gray)
    cv2.imshow("Edges", edges)





    cv2.waitKey(0)
    cv2.destroyAllWindows()
    h,w,c = img.shape
    print(h,w,c)






