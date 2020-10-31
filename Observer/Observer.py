from abc import ABC,abstractmethod

class Youtube():
    def __init__(self):
        self.list=[]

    def subscribe(self,iObj):
        self.list.append(iObj)

    def unSubscribe(self,iObj):
        self.list.remove(iObj)

    def notify(self):
        for i in self.list:
            i.getNotification()

    def videoUpload(self):
        print('video added')
        self.notify()


class Iobj(ABC):
    @abstractmethod
    def getNotification(self):
        pass

class EmailSubs(Iobj):

    def getNotification(self):
        print('Email Subscribe')


class Account(Iobj):

    def getNotification(self):
        print('Account Subscribe')


class SMS(Iobj):

    def getNotification(self):
        print('SMS Subscribe')

s=SMS()
e=EmailSubs()
a=Account()
y=Youtube()
y.subscribe(s)
y.subscribe(e)
y.subscribe(a)
y.videoUpload()
y.unSubscribe(a)
y.videoUpload()