#!/usr/bin/env python3
'''Assignment 4 Part 1'''
print(__doc__)

from typing import IO

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
        
def drawCircleLine(f: IO[str], t: int, c: Circle):
    '''drawCircle method'''
    ts: str = "   " * t
    line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line}\n")
        
def genCircleArt(f: IO[str], t: int):
   '''genCircleArt method'''
   drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((150,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((250,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
   drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
   
        

class Rectangle:
    '''Rectangle class'''
    def __init__(self, rect: tuple, col: tuple):
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

def drawRectangleLine(f: IO[str], t: int, r: Rectangle):
    '''drawRectangle method'''
    ts: str = "   " * t
    line: str = f'<rect x="{r.x}" y="{r.y}" width="{r.width}" height="{r.height}" fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
    f.write(f"{ts}{line}\n")

def genRectangleArt(f: IO[str], t: int):
    '''genRectangleArt method'''
    drawRectangleLine(f, t, Rectangle((50,250,60,60), (0,100,155,1.0)))
    drawRectangleLine(f, t, Rectangle((150,250,30,30), (120,0,205,1.0)))
    drawRectangleLine(f, t, Rectangle((250,250,60,60), (0,0,205,1.0)))
    drawRectangleLine(f, t, Rectangle((350,250,30,30), (40,12,5,1.0)))
    drawRectangleLine(f, t, Rectangle((450,250,10,10), (232,0,255,1.0)))



class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, fnam:str):
        self.file: IO[str] = open(fnam, "w")

def writeHTMLcomment(f: ProEpilogue, t: int, com: str):
    '''writeHTMLcomment method'''
    ts: str = "   " * t
    f.file.write(f'{ts}<!--{com}-->\n')       

def openSVGcanvas(f: ProEpilogue, t: int, canvas: tuple):
     '''openSVGcanvas method'''
     ts: str = "   " * t
     writeHTMLcomment(f, t, "Define SVG drawing box")
     f.file.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

def closeSVGcanvas(f: ProEpilogue, t: int):
    '''closeSVGcanvas method'''
    ts: str = "   " * t
    f.file.write(f'{ts}</svg>\n')
    f.file.write(f'</body>\n')
    f.file.write(f'</html>\n')
    f.file.close()

def writeHTMLline(f: ProEpilogue, t: int, line: str):
     '''writeLineHTML method'''
     ts = "   " * t
     f.file.write(f"{ts}{line}\n")

def writeHTMLHeader(f: ProEpilogue, winTitle: str):
    '''writeHeadHTML method'''
    writeHTMLline(f, 0, "<html>")
    writeHTMLline(f, 0, "<head>")
    writeHTMLline(f, 1, f"<title>{winTitle}</title>")
    writeHTMLline(f, 0, "</head>")
    writeHTMLline(f, 0, "<body>")

def writeHTMLfile(f: ProEpilogue):
    '''writeHTMLfile method'''
    winTitle = "My Art"
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (500,300))
    



def main():
    '''main method'''
    fnam: str = "myPart1Art.html"
    Epilogue = ProEpilogue(fnam)
    writeHTMLfile(Epilogue)
    genCircleArt(Epilogue.file,2)
    genRectangleArt(Epilogue.file,2)
    closeSVGcanvas(Epilogue,1)
    
if __name__ == '__main__':
    main()
                                                                                                                                                                                                                                                                                                        
