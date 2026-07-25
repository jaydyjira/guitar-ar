import cv2
import numpy as np

first_four_clicks = []
labels = ["nut top", "nut bottom", "fret 12 top", "fret 12 bottom"]

def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at: {x}, {y}")
        if len(first_four_clicks) < 4:
            first_four_clicks.append((x, y))
            print(f"First four clicks: {first_four_clicks}")

cap = cv2.VideoCapture(0)

cv2.namedWindow("My video")                       # make the window once
cv2.setMouseCallback("My video", on_click)          # attach the click handler once

while True:
    ok, frame = cap.read()
    if not ok:
        print("Cannot read from camera.")
        break
    frame = cv2.flip(frame, 1)
    if len(first_four_clicks) < 4:
        instruction = f"Click: {labels[len(first_four_clicks)]}"
    else:
        instruction = "All 4 points collected!"
        
    if len(first_four_clicks) == 4:
        # Transform the list of clicks into a NumPy array with dtype float32 (OpenCV requires float32 for perspective transforms)
        src_points = np.array(first_four_clicks, dtype=np.float32)

        # Real image to flattened image
        dst_points = np.array([
            [0, 0],       # nut top    -> top-left
            [0, 300],     # nut bottom -> bottom-left
            [800, 0],     # fret12 top    -> top-right
            [800, 300],   # fret12 bottom -> bottom-right
        ], dtype=np.float32)

        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        flattened = cv2.warpPerspective(frame, matrix, (800, 300))

        cv2.imshow("Flattened fretboard", flattened)

        # Flattened rectangle to real image
        matrix_inv = cv2.getPerspectiveTransform(dst_points, src_points) # just two arguments swapped
        overlay = np.zeros((300, 800, 3), dtype=np.uint8)
        cv2.rectangle(overlay, (0, 0), (800, 300), (0, 255, 0), 5)
        warped_overlay = cv2.warpPerspective(overlay, matrix_inv, (frame.shape[1], frame.shape[0]))
        frame = cv2.addWeighted(frame, 1, warped_overlay, 1, 0)
        
    cv2.putText(frame, instruction, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("My video", frame)          # show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # this ONE line renders AND checks for q
        break

cap.release()
cv2.destroyAllWindows()