#!/usr/bin/env python3
# coding: utf-8

### Functions & Procedures
def rectQualities():
    fill(None)
    stroke(0)
    strokeWidth(.5)

def lozangeQualities():
    fill(.5)
    stroke(None)

### Variables
side = 20
amount = 5

### Instructions
size(100, 100)

stroke(0)
fill(None)
for eachJ in range(amount):
    save()
    for eachI in range(amount):
        rectQualities()
        rect(0, 0, side,side)

        with savedState():
            translate(side/2, side/2)
            rotate(45)
            lozangeQualities()
            rect(-side/2, -side/2, side, side)

        translate(side, 0)
    restore()
    translate(0, side)

