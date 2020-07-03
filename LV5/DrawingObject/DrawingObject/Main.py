import GrafLik as GrLik
Polygon = GrLik.Polygon
Line = GrLik.Line
Triangle = GrLik.Triangle
Rectangle = GrLik.Rectangle
Circle = GrLik.Circle
Ellipse = GrLik.Ellipse
Polygon = GrLik.Polygon

from tkinter import *
from tkinter import filedialog

class Application(Frame):
    def CreateWidgets(self):
        self.canvas = Canvas(height = 600, width = 800, background = 'Gray')
        self.canvas.pack()


    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.CreateWidgets()



    def drawFromFile(self, cmdFile):
        for line in cmdFile:
            self.drawObj(line.strip())



    def drawObj(self, cmdStr):
        splitStr = cmdStr.strip().split(' ')
        objType = splitStr[0]
        objeColor = splitStr[1]
        objCord = tuple(float(ea) for ea in splitStr[2:])
        print(objCord)
        if objType == 'Line':
            line = Line(objeColor, objCord[0],objCord[1],objCord[2],objCord[3])
            line.Draw(self.canvas)
        elif objType == 'Triangle':
            triangle = Triangle(objeColor,objCord[0],objCord[1],objCord[2],objCord[3],objCord[4],objCord[5] )
            triangle.Draw(self.canvas)
        elif objType == 'Rectangle':
            rectangle = Rectangle(objeColor,objCord[0],objCord[1],objCord[2],objCord[3])
            rectangle.Draw(self.canvas)
        elif objType == 'Circle':
            circle = Circle(objeColor, objCord[0],objCord[1],objCord[2])
            circle.Draw(self.canvas)
        elif objType == 'Ellipse':
            ellipse = Ellipse(objeColor, objCord[0],objCord[1],objCord[2],objCord[3])
            ellipse.Draw(self.canvas)
        elif objType == 'Polygon':
            coordinates = [float(i) for i in objCord]
            polygon = Polygon(objeColor, coordinates)
            polygon.Draw(self.canvas)



def fileOpen():
    file = filedialog.askopenfile(mode='r')
    app.drawFromFile(file)
def fileExit():
    root.destroy()

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    m = Menu(root)
    filemenu = Menu(m, tearoff=0)
    filemenu.add_command(label="Open", command = fileOpen)
    filemenu.add_command(label="Quit", command = fileExit)
    m.add_cascade(label="File", menu=filemenu)
    root.config(menu=m)
    app.mainloop()