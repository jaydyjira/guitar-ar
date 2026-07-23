import cv2

cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not ok:
        print("Cannot read from camera.")
        break

    cv2.imshow("My video", frame)          # show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # this ONE line renders AND checks for q
        break

cap.release()
cv2.destroyAllWindows()