

import turtle
import pygame

from abc import abstractmethod,ABC

skk = turtle.Turtle()

class IShape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Line(IShape):

    def draw(self,pos):
        skk.setpos(0, 100)
        skk.goto(-100, 100)

class Circle(IShape):

    def draw(self):
        print('draw circle')

class CompositeShape(IShape,ABC):
    def __init__(self):
        self.list=[]
    @abstractmethod
    def buildShape(self):
        pass

    def draw(self):
        self.buildShape()
        for i in self.list:
            i.draw()

class Rectangel(CompositeShape):

    def buildShape(self):
        l=Line()
        self.list.append(l)
        self.list.append(l)
        self.list.append(l)
        self.list.append(l)


class Triangle(CompositeShape):

    def buildShape(self):
        l = Line()
        self.list.append(l)
        self.list.append(l)
        self.list.append(l)


class Flag(CompositeShape):
    def buildShape(self):
        r=Rectangel()
        c=Circle()
        self.list.append(r)
        self.list.append(c)






for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()


skk.goto(-100,-88)
skk.setpos(100,100)
skk.setpos(100,0)
skk.setpos(0,0)
skk.left(60)
skk.forward(80)
turtle.done()

'''from abc import abstractmethod,ABC

class IShape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Line(IShape):

    def draw(self):
        print('draw line')

class Circle(IShape):

    def draw(self):
        print('draw circle')

class CompositeShape(IShape,ABC):
    def __init__(self):
        self.list=[]
    @abstractmethod
    def buildShape(self):
        pass

    def draw(self):
        self.buildShape()
        for i in self.list:
            i.draw()

class Rectangel(CompositeShape):

    def buildShape(self):
        l=Line()
        self.list.append(l)
        self.list.append(l)
        self.list.append(l)
        self.list.append(l)


class Triangle(CompositeShape):

    def buildShape(self):
        l = Line()
        self.list.append(l)
        self.list.append(l)
        self.list.append(l)


class Flag(CompositeShape):
    def buildShape(self):
        r=Rectangel()
        c=Circle()
        self.list.append(r)
        self.list.append(c)


f=Flag()
f.draw()'''