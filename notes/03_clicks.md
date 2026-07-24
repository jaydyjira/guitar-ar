# Function
```
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at: {x}, {y}")
```
This is a function — a named block of code you define once, and OpenCV will call it for you automatically every time something happens in the window (this pattern is called a "callback" — you're not calling this function yourself, you're handing it to OpenCV and saying "run this whenever a mouse event happens"). Its four parameters are fixed — OpenCV always passes exactly these four things, whether you use them all or not:
`event` — what kind of mouse thing happened (moved, clicked, released...)
`x, y` — where it happened, in pixel coordinates — this is the part you actually want
`flags, param` — extra info you won't need yet

# Tools
`cv2.EVENT_LBUTTONDOWN` "left mouse button pressed down."
`cv2.setMouseCallback("My video", on_click)` is the line that actually says "hey OpenCV, use on_click to handle mouse events on this specific window." The window name has to match exactly what you pass to imshow.
`cv2.namedWindow` creates an empty, nameless-content window in advance, before you have any image to put in it — useful when you want to configure the window itself (resizable, fullscreen, etc.) before anything's shown. It's not a renaming tool — the name was never the issue.