# Concept
The last concept was transforming real image -> flattened image
This one is kinda same but reverse!
So create a rectangle in flattened image and then transform it back to the real perspective.
Flattened image -> real image

# Tools
`matrix_inv = cv2.getPerspectiveTransform(dst_points, src_points)`
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