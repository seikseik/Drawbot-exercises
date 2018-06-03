canvas = 100
size( canvas,canvas)

side=10
color=0


maxJ = height()/side -1
maxI =width()/side -1

jj=0
while jj*side <= height()-side:
    ii=0 
    while ii*side <= width()-side:
        gray= 1-(ii+jj)/(maxJ+maxI)
        fill(gray)
        rect(ii*side,jj*side,side,side)
        ii += 1
    jj +=1 
    