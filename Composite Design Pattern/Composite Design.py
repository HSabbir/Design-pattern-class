
from tkinter import Tk, Canvas, Frame, BOTH

from abc import abstractmethod,ABC

top = Tk()

top.geometry("400x250+300+300")

# creating a simple canvas
c = Canvas()

class IShape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Line(IShape):

    def __init__(self,p1,p2):
        #super.__init__()
        self.x1=p1[0]
        self.x2=p2[0]
        self.y1=p1[1]
        self.y2=p2[1]

    def draw(self):
        c.create_line(self.x1,self.y1,self.x2,self.y2)

class Circle(IShape):


    def draw(self,p1,p2):
        c.create_oval(p1[0],p1[1],p2[0],p2[1])

class CompositeShape(IShape,ABC):
    def __init__(self):
        self.list=[]
    @abstractmethod
    def buildShape(self):
        pass

    def draw(self,p):
        self.buildShape(p)
        for i in self.list:
            i.draw()

class Rectangel(CompositeShape):

    def buildShape(self,p):
        l1 = Line(p[0], p[1])
        l2 = Line(p[1], p[2])
        l3 = Line(p[2], p[3])
        l4 = Line(p[3],p[4])
        # l1.draw()
        self.list.append(l1)
        self.list.append(l2)
        self.list.append(l3)
        self.list.append(l4)


class Triangle(CompositeShape):

    '''def __init__(self,p1,p2,p3):
        self.point=[p1,p2,p3]'''

    def buildShape(self,p):
        #print(p1)
        l1 = Line(p[0],p[1])
        l2 = Line(p[1],p[2])
        l3 = Line(p[2],p[0])
        #l1.draw()
        self.list.append(l1)
        self.list.append(l2)
        self.list.append(l3)


class Flag(CompositeShape):
    def buildShape(self):
        r=Rectangel()
        c=Circle()
        self.list.append(r)
        self.list.append(c)



t=Rectangel()
t.draw([[10,20],[20,20],[40,50],[10,20]])
#t.draw()
c.pack()
top.mainloop()


'''class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.master.title("Shape")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 36)
        canvas.create_line(300, 35, 300, 200, )
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()'''



'''top = Tk()

top.geometry("200x200")

# creating a simple canvas
c = Canvas(top, bg="pink", height="200", width=200)


def draw():

    c.create_line(15, 25, 200, 36)
    c.pack()
    top.mainloop()

draw()'''