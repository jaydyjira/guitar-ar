# Concept
You have four points describing a tilted, skewed rectangle somewhere in your camera image — call that the "source."
You also get to invent a perfectly clean rectangle, straight on, any size you like — call that the "destination."
A perspective transform is a single matrix that describes exactly how to warp one into the other. Once you have that matrix, you can apply it to the whole image, not just your four points — and the result is your guitar neck redrawn as if the camera were looking at it perfectly straight-on, no matter how it was actually tilted or rotated when you clicked.

# Questions
## Why don't I store the coordinates in np.array at the first place?
Ans: NumPy arrays are built for a fixed size, known upfront. Python lists are built for growing one item at a time
If you tried to keep a NumPy array and grow it click by click, you'd have to use np.append() or similar, **which secretly recreates the entire array from scratch every single call**, because NumPy arrays aren't actually resizable in memory

## Does the final coordinates has to always be (0,0), (0,300), (800,0), (800,300)?
Ans: No. and they r not the corner of the frame. From `warpPerspective(frame, matrix, (800, 300))`, it creates an output canvas that is exactly **800×300 pixels**, so Your four destination points — (0,0), (0,300), (800,0), (800,300) — are the four literal corners of that exact canvas.

# Tools
`np.array(first_four_clicks, dtype=np.float32)`
OpenCV's math functions want a NumPy array of decimal numbers (float32), not plain integers. This line just repackages what you already have into the shape OpenCV expects.

`dst_points = np.array([
    [0, 0],       # nut top    -> top-left
    [0, 300],     # nut bottom -> bottom-left
    [800, 0],     # fret12 top    -> top-right
    [800, 300],   # fret12 bottom -> bottom-right
], dtype=np.float32)`
this is you designing the clean output. You're saying "I want a rectangle 800 pixels wide, 300 pixels tall, and here's which corner of it each of my four clicks should map to." **Order matters enormously here** dst_points[0] must correspond to whatever src_points[0] is

`cv2.getPerspectiveTransform(src_points, dst_points)`
this is the function that actually computes the matrix: "what transform turns these source points into those destination points?" You don't build the matrix yourself; you just hand over the before-and-after points and OpenCV solves for it.

`cv2.warpPerspective(frame, matrix, (800, 300))`
apply that matrix to the entire frame, and crop/resize the result to your chosen output size, (800, 300). This is the line that actually produces your flattened image.