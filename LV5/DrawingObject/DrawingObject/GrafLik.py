class GrafLik:
    color  = 'black'
    xcord = 1
    ycord = 1
    def __init__(self, color, x, y ):
        self.SetColor(color)
        self.xcord = x
        self.ycord = y
    def SetColor (self, color):
        self.color = color
    def GetColor(self):
        return self.color
    def Draw (self):
        return 0


class Line(GrafLik):
    xcordL = 1
    ycordL = 1
    def __init__(self, color, x1, y1, x2, y2):
        GrafLik.__init__(self, color, x1, y1)
        self.xcordL = x2
        self.ycordL = y2
    def Draw(self, tarCanvas):
        tarCanvas.create_line(self.xcord, self.ycord, self.xcordL, self.ycordL, fill = self.color, width = 1)



class Triangle(Line):
    xcordT = 1
    ycordT = 1
    def __init__(self, color, x1, y1, x2, y2, x3, y3):
        Line.__init__(self, color, x1,y2,x2,y2)
        self.xcordT = x3
        self.ycordT = y3
    def Draw(self, tarCanvas):
        tarCanvas.create_line(self.xcord, self.ycord, self.xcordL, self.ycordL, fill = self.color, width = 1)
        tarCanvas.create_line(self.xcordL, self.ycordL, self.xcordT, self.ycordT, fill = self.color, width = 1)
        tarCanvas.create_line(self.xcordT, self.ycordT, self.xcord, self.ycord, fill = self.color, width = 1)


class Rectangle(GrafLik):
    height = 0
    width = 0
    xcordR = 1
    ycordR = 1
    def __init__(self, color, x, y, height, width):
        GrafLik.__init__(self, color, x, y)
        self.height = height
        self.width = width
        self.xcordR = self.xcord + width
        self.ycordR=self.ycord+height
    def Draw(self, tarCanvas):
        tarCanvas.create_rectangle(self.xcord, self.ycord, self.xcordR, self.ycordR, outline = self.color, fill = '', width = 1)


class Circle(GrafLik):
    xcordC=1
    ycordC=1
    def __init__(self, color, x, y, radius):
        GrafLik.__init__(self, color, x-radius, y-radius)
        self.xcordC = x + radius
        self.ycordC = y + radius
    def Draw(self, tarCanvas):
        tarCanvas.create_oval(self.xcord, self.ycord, self.xcordC, self.ycordC, outline=self.color, fill='', width=1)


class Ellipse(Circle):
    def __init__(self, color, x, y, _x, _y):
        GrafLik.__init__(self, color, x-_x, y-_y)
        self.xcordC=x+_x
        self.ycordC=y+_y
    def Draw(self, tarCanvas):
        tarCanvas.create_oval(self.xcord, self.ycord, self.xcordC, self.ycordC, outline=self.color, fill='', width=1)


class Polygon(GrafLik):
    points = None
    def __init__(self, color, points):
        GrafLik.__init__(self, color, None, None)
        self.points = points
    def Draw(self, tarCanvas):
        tarCanvas.create_polygon(self.points, outline=self.color, fill='', width=1)
