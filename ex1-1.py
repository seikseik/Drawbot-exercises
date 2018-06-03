canvas=150
size(canvas,canvas)
a=canvas/6

rect(a,a,a,a)
rect(canvas-2*a,a,a,a)
rect(a,canvas-2*a,a,a)
rect(canvas-2*a,canvas-2*a,a,a)

stroke(0)
line((canvas/2,0),(canvas/2,canvas))
line((0,canvas/2),(canvas,canvas/2))
