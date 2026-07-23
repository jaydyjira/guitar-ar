# Concept
So I just learned that video showing on the screen in this project is the loop of still photos for every 1 millisecond

# Code
`import cv2`
Don't forget to import cv2

`cap = cv2.VideoCapture(0)`
open a line to camera number 0
cap is now your handle to it — like picking up a phone connected to the camera.

`ok, frame = cap.read()`
ask the camera for a photo `ok` check if it works and `frame` is the actual photo

`cap.release()`
hang up the phone. Let go of the camera so other apps can use it. Polite and important.

`cv2.imshow("My first photo", frame)`
pop open a window titled "My first photo" and show the photo inside it.

`cv2.waitKey(0)`
freeze right here and wait until you press any key. Without this line, the window would flash open and vanish in a blink. The 0 means "wait forever."

`cv2.destroyAllWindows()`
once you press a key, close the window cleanly.

`if cv2.waitKey(1) & 0xFF == ord('q'):`
pause 1 millisecond and check if a key was pressed to get out of the while loop.

`frame = cv2.flip(frame, 1)`
1 = flip horizontally (left-right) — this is the mirror effect you want.
0 = flip vertically (upside down) — not what you want here.
-1 = flip both at once.