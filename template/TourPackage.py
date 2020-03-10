'''from abc import abstractmethod,ABC
class TourPackage(ABC):

    def hire(self):
        self.jabo(),self.ghurbo(),self.firbo()

    @abstractmethod
    def jabo(self):
        pass

    @abstractmethod
    def ghurbo(self):
        pass

    @abstractmethod
    def firbo(self):
        pass

class Deluxe(TourPackage):
    def jabo(self):
        print("Jassi Ac te")
    def ghurbo(self):
        print('ghursi 4 star e')
    def firbo(self):
        print('firci AC  te')

class Luxury(TourPackage):
    def jabo(self):
        print("Jassi AIR E")
    def ghurbo(self):
        print('ghursi 5 star e')
    def firbo(self):
        print('firci Air E')

client1= Luxury()
client1.hire()'''

from tkinter import Tk, Canvas, Frame, BOTH

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

master.mainloop()