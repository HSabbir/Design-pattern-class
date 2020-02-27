from abc import abstractmethod,ABC
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
client1.hire()