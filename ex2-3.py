canvas = 100
size(canvas,canvas)

fill(None)
strokeWidth(.5)

ii=0

NN = ii, canvas
WW = 0, ii
SS = canvas-ii, 0
EE = canvas, canvas-ii


while ii <= canvas:
    
    line(NN,EE)
    line(EE,SS)
    line(SS,WW)
    line(WW,NN)
    
    
    ii+=10 