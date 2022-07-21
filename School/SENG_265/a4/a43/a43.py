#!/usr/bin/env python3
'''Assignment 4 Part 3'''
print(__doc__)

from a41_3 import *
from a42_3 import ArtConfig

def makeArt(num: int,fname: str):
    '''makeArt method'''
    ProEp = ProEpilogue(fname)
    ProEp.writeHTMLfile()
    

    Art = ArtConfig(num)
    Art.createLists()
    i = 0
    c = Circle(0,0,0,0,0,0,0)
    r = Rectangle(0,0,0,0,0,0,0,0)
    while i < num:
        if Art.SHA[i] == 0:
            c.cx = Art.X[i]
            c.cy = Art.Y[i]
            c.rad = Art.RAD[i]
            c.red = Art.R[i]
            c.green = Art.G[i]
            c.blue = Art.B[i]
            c.op = Art.OP[i]
            c.drawCircleLine(ProEp.file,2)
        elif Art.SHA[i] == 1:
            r.x = Art.X[i]
            r.y = Art.Y[i]
            r.width = Art.W[i]
            r.height = Art.H[i]
            r.red = Art.R[i]
            r.green = Art.G[i]
            r.blue = Art.B[i]
            r.op = Art.OP[i]
            r.drawRectangleLine(ProEp.file,2)
        i+=1

    ProEp.closeSVGcanvas(1)


def main():
    '''main method'''
    makeArt(1000,"myart1.html")
    makeArt(2000,"myart2.html")
    makeArt(3000,"myart3.html")

if __name__ == '__main__':
    main()