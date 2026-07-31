# Concept
The last concept was transforming real image -> flattened image
This one is kinda same but reverse!
So create a rectangle in flattened image and then transform it back to the real perspective.
Flattened image -> real image

# Tools
`cv2.getPerspectiveTransform(dst_points, src_points)`
just swap the src_points and dst_points

`overlay = np.zeros((300, 800, 3), dtype=np.uint8)`
makes a blank black image
300 - height
800 - width
3 - **channels**
dtype=np.uint8 - says each of those numbers is a whole number from 0 to 255 — the standard range for image brightness, where 0 is none and 255 is full.
**What is a channels?**
Ans: A color pixel stores three numbers — blue, green, red. A channel is one of those layers
A color image is really three stacked grids — a blue grid, a green grid, a red grid — and each pixel's color comes from combining its value in all three.

`cv2.rectangle(overlay, (0, 0), (800, 300), (0, 255, 0), 5)`
draws a green outline border around the whole thing

Then
`warped_overlay = cv2.warpPerspective(overlay, matrix_inv, (frame.shape[1], frame.shape[0]))
frame = cv2.addWeighted(frame, 1, warped_overlay, 1, 0)`

`cv2.addWeighted(image1, weight1, image2, weight2, gamma)`
Combine two frames into one
the formula is **result = image1 × weight1 + image2 × weight2 + gamma**
image1, image2 — the two images to blend. **They must be the same size and same number of channels** — this is exactly what crashed when you removed the 3.
weight1, weight2 — how strongly each contributes. 1 means full strength, 0.5 means half, 0 means invisible.
gamma — a flat brightness added to everything afterward. Usually 0.
**Note** `cv2.addWeighted(frame, 1, warped_overlay, 1, 0)` and warped_overlay is a zeros matrix and have green outline. **Adding 0 to a pixel leaves it unchanged.** So the black regions(0) vanish into your frame while the green line (255 in the green channel) adds visibly.

**But this has a problem**
The rectangle I drew is gonna be stretched to the smaller real image, so the 5 px line can shrink to 2 px line and it doesn't show on the screen.
**Instead**
Map the points from flattened image to the real image first and then draw the lines connecting each dot later.

`corners = np.array([[[0,0], [0,300], [800,300], [800,0]]], dtype=np.float32)
real_corners = cv2.perspectiveTransform(corners, matrix_inv)
cv2.polylines(frame, [real_corners.astype(np.int32)], True, (0,255,0), 2)`

`cv2.polylines(frame, [real_corners.astype(np.int32)], True, (0,255,0), 2)`
frame — draw onto this image (same as circle and putText)
`[real_corners...]` — the list of points to connect, in order. Note it's wrapped in [ ] because polylines can draw several separate shapes at once, so it expects a list of point-arrays.
True — "closed": connect the last point back to the first, sealing the shape. False would leave it as an open zigzag.
(0,255,0) and 2 — color and thickness, same as always.

**The .astype(np.int32) matters:** perspectiveTransform returns decimals, but drawing functions need whole-number pixel coordinates. That converts them.
