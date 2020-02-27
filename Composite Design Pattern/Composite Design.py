from abc import abstractmethod,ABC

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
f.draw()