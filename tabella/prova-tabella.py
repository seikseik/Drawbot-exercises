
# coding: utf-8

#dubbi e domade:
    #a cosa serve return?
    #selettori:


#################
# Display Table #
#################

### Modules

### Constants

### Functions & Procedures
def loadTable(csvPath):
    with open(csvPath, 'r') as csvFile:
        someColors = [nn.strip() for nn in csvFile.readlines()]
    return someColors




def convert2rgb(colorHex):
    rr = colorHex[:2]
    gg = colorHex[2:4]
    bb = colorHex[4:]
    return int(rr, 16), int(gg, 16), int(bb, 16)

def convert2hex(colorHex):
    return '#{}'.format(colorHex.upper())
    

def convert2dbColor(colorHex):
    rr = colorHex[:2]
    gg = colorHex[2:4]
    bb = colorHex[4:]
    return int(rr, 16)/255, int(gg, 16)/255, int(bb, 16)/255

#converti il valore di dbcolor in %
def convert2ratio(colorHex):
    dbColor=convert2dbColor(colorHex)
    rr=dbColor[0]
    gg=dbColor[1]
    bb=dbColor[2]
    return '{:.0%}'.format(rr), '{:.0%}'.format(gg),'{:.0%}'.format(bb)

    

### Variables
csvPath = 'webSafeColor.csv'
margin = 20
### Instructions
someColors = loadTable(csvPath)

#print(convert2hex(someColors))
ii=0
newPage('A4')

while someColors:
    
    aColor = someColors.pop()
    print(convert2rgb(aColor))
    dbColor = convert2dbColor(aColor)
    fill(*dbColor)
    
    hexColor = convert2hex(aColor)
    rgbColor = convert2rgb(aColor)
    ratioColor = convert2ratio(aColor)
    
    fill(*dbColor)
    rect(20,(height()-40)-ii,50,20)
    
    
    fill(0)
    
    text(str(rgbColor),(160,(height()-margin*2)-ii))
    text(str(ratioColor),(260,(height()-margin*2)-ii))
    text(hexColor,(90,(height()-margin*2)-ii))
    
    ii+=25 
       
    if ii>height()-margin*3:
        newPage('A4')
        ii=0
    
            
    




