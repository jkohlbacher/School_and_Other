from typing import IO

class Circle:
    '''Circle class'''
    def __init__(self, cx: int, cy: int, rad: int, red: int, green: int, blue: int, op: float):
        self.cx: int = cx
        self.cy: int = cy
        self.rad: int = rad
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self.op: float = op
        
        
    def drawCircleLine(self,f: IO[str], t: int):
        '''drawCircle method'''
        ts: str = "   " * t
        line: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line}\n")
        
    
        

class Rectangle:
    '''Rectangle class'''
    def __init__(self, x: int, y: int, width: int, height: int, red: int, green: int, blue: int, op: float ):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
        self.op: float = op

    def drawRectangleLine(self,f: IO[str], t: int):
        '''drawRectangle method'''
        ts: str = "   " * t
        line: str = f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line}\n")
  

class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, fnam: str):
        self.file: IO[str] = open(fnam, "w")

    def writeHTMLcomment(self, t: int, com: str):
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        self.file.write(f'{ts}<!--{com}-->\n')       

    def openSVGcanvas(self, t: int, canvas: tuple):
        '''openSVGcanvas method'''
        ts: str = "   " * t
        self.writeHTMLcomment(t, "Define SVG drawing box")
        self.file.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def closeSVGcanvas(self, t: int):
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        self.file.write(f'{ts}</svg>\n')
        self.file.write(f'</body>\n')
        self.file.write(f'</html>\n')
        self.file.close()

    def writeHTMLline(self, t: int, line: str):
        '''writeLineHTML method'''
        ts = "   " * t
        self.file.write(f"{ts}{line}\n")

    def writeHTMLHeader(self, winTitle: str):
        '''writeHeadHTML method'''
        self.writeHTMLline(0, "<html>")
        self.writeHTMLline(0, "<head>")
        self.writeHTMLline(1, f"<title>{winTitle}</title>")
        self.writeHTMLline(0, "</head>")
        self.writeHTMLline(0, "<body>")

    def writeHTMLfile(self):
        '''writeHTMLfile method'''
        winTitle = "My Art"
        self.writeHTMLHeader(winTitle)
        self.openSVGcanvas(1, (550,300))
    


