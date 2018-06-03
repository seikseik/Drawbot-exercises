#!/usr/bin/env python3
# coding: utf-8

######################
# Python Boilerplate #
######################

### Modules
from colorsys import hls_to_rgb

### Constants

### Functions & Procedures
def typeQualities():
    font('InputMono-Regular')
    fontSize(12)
    fill(0)
    stroke(None)

def drawColorRings(innerRadius, ringAmount, ringThickness, offsetCaption, fixedParameter):
    assert fixedParameter['type'] in ['luminosity', 'saturation'], 'this type of fixed parameter is not accepted'

    for eachDegree in range(360):
        strokeWidth(ringThickness)
        hh = eachDegree/360
        for eachRing in range(ringAmount):

            if fixedParameter['type'] == 'luminosity':
                ll = fixedParameter['value']
                ss = eachRing/(ringAmount-1)
            else:
                ss = fixedParameter['value']
                ll = eachRing/(ringAmount-1)

            selectedColor = hls_to_rgb(hh, ll, ss)
            stroke(*selectedColor)
            newPath()
            arcRadius = innerRadius+(eachRing*ringThickness)
            arc((0, 0), arcRadius, eachDegree, eachDegree+1, clockwise=False)
            drawPath()

        if eachDegree % 10 == 0:
            typeQualities()
            with savedState():
                rotate(eachDegree)
                translate(arcRadius+offsetCaption, 0)
                text('{: >3d}'.format(eachDegree), (0, 0))

### Variables

### Instructions
size(500, 500)
translate(width()/2, height()/2)

drawColorRings(innerRadius=30,
               ringAmount=8,
               ringThickness=18,
               offsetCaption=10,
               fixedParameter={'type': 'luminosity', 'value': .6})
