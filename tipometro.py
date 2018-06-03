
size(100,100)


stroke(0)
strokeWidth(.1)

x=10
xx=50
jj=0

while jj<100:
    ii=0
    while ii<100:
        line((x,ii),(x+7,ii))
        ii+=3    
    line((x,jj),(x+5,jj))
    jj+=1
    
aa=0
while aa<100:
    bb=0
    while bb<100:
        line((xx,bb),(xx+10,bb))
        bb+=5+(5*0.64722)   
    line((xx,aa),(xx+5,aa))
    aa+=1+0.64722
    
    