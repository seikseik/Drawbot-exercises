canvas = 100
side=10

size (canvas,canvas)

jj = 0
while jj*side <= height()-side:
    ii=0
    while ii*side <= width()-side:
        if(ii+jj) % 2 ==0:
            fill(0)
        else:
            fill(1)
        rect(ii*side, jj*side,side,side)
        ii += 1
    jj += 1 
    
    
