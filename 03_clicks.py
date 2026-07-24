import cv2

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

    cv2.putText(frame, instruction, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("My video", frame)          # show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # this ONE line renders AND checks for q
        break

cap.release()
cv2.destroyAllWindows()