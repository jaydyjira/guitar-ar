import cv2

cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not ok:
        print("Cannot read from camera.")
        break
    frame = cv2.flip(frame, 1)
    cv2.circle(frame, (50,50), 3, (0,255,0), -1) # draw a green dot at (50,50)

    cv2.putText(frame, "67", (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2) # draw a black "67" at (50,40)

    cv2.imshow("My video", frame)          # show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # this ONE line renders AND checks for q
        break

cap.release()
cv2.destroyAllWindows()