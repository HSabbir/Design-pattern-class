from Interface import implements, Interface

class Payment(Interface):
    def execute(self):
        pass


class Bkash(implements(Payment)):
    def execute(self):
        print("Bkash")

class Rocket(implements(Payment)):
    def execute(self):
        print("Rocket")
class Cash(implements(Payment)):
    def execute(self):
        print("Cash On")





'''class MyInterface(Interface):

    def method1(self, x):
        pass

    def method2(self, x, y):
        pass


class MyClass(implements(MyInterface)):

    def method1(self, x):
        return x * 2

    def method2(self, x, y):
        return x + y'''