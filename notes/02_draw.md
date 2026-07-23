# Tools
## Tool 1 Draw a circle
`cv2.circle(frame, (300, 200), 20, (0, 255, 0), -1)`

`frame`
draw onto this image. (This is why order matters: draw before you imshow it, or your drawing won't show up yet.)

`(300, 200)`
the center point, as (x, y). In images, (0,0) is the top-left corner, x grows rightward, y grows downward (the opposite of a math graph — a classic gotcha, so file that away).

`20`
radius in pixel

`(0, 255, 0)`
the color. Here's the trap: OpenCV colors are (Blue, Green, Red) — backwards from how you'd normally say "RGB." So (0, 255, 0) means "no blue, full green, no red" = green. (0, 0, 255) would be red. Yes, this catches everyone at least once.

`-1` the thickness. A positive number draws just an outline that thick; -1 is special and means "fill the whole shape solid."

## Tool 2 Draw text
`cv2.putText(frame, "hello", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)`
Same pattern: image to draw on, the text itself, the position (this time it's roughly the bottom-left of where the text starts), then a font choice (just always use that one, it's the standard default), the size, the color (still Blue-Green-Red!), and the line thickness.