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
        

"""
import cv2 — load the OpenCV toolbox so we can use its commands. 
(cv2 is just OpenCV's internal nickname.)

cap = cv2.VideoCapture(0) — open a line to camera number 0, your built-in webcam. 
cap is now your handle to it — like picking up a phone connected to the camera.

ok, frame = cap.read() — ask the camera for one photo. Notice it hands back two things at once
: ok (True if it worked) and frame (the actual photo). Getting two answers from one line is a 
normal Python move. That frame, by the way, is secretly just a giant grid of numbers
 — the brightness of every pixel — which is exactly why NumPy mattered way back.

cap.release() — hang up the phone. Let go of the camera so other apps can use it. 
Polite and important.

if not ok: — a safety check. If the camera didn't hand us a photo, print a helpful message 
instead of crashing.

cv2.imshow("My first photo", frame) — pop open a window titled "My first photo" and 
show the photo inside it.

cv2.waitKey(0) — freeze right here and wait until you press any key. Without this line,
the window would flash open and vanish in a blink. The 0 means "wait forever."

cv2.destroyAllWindows() — once you press a key, close the window cleanly.
"""