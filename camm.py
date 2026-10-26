import cv2

def cam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # msv = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
        msv = frame
        bsv = cv2.cvtColor(msv, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(bsv, 0, 255, cv2.THRESH_BINARY)
        counter, hi = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(msv, counter, -1, (255,255,255),10)
        re = cv2.resize(msv, (1500,1000))
        if not ret:
            print("Could not read frame")

        # cv2.imshow("Webcam feed", bsv)
        cv2.imshow("WEE", msv)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Qutting...")
            break
    cap.release()
    cv2.destroyAllWindows()
cam()
