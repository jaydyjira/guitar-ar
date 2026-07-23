import cv2

print("Checking camera numbers 0 to 3...")

for number in range(4):          # try 0, 1, 2, 3
    cap = cv2.VideoCapture(number)
    ok, frame = cap.read()       # can we actually get a photo from it?
    cap.release()

    if ok:
        print(f"  Camera {number}: WORKS")
    else:
        print(f"  Camera {number}: nothing here")

print("Done. Use the lowest number that says WORKS.")