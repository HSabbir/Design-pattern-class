from abc import ABC,abstractmethod

class Auctioner():
    def __init__(self,startBid):
        self.highest_bid = startBid
        self.list=[]

    def subscribe(self,iObj):
        self.list.append(iObj)

    def unSubscribe(self,iObj):
        self.list.remove(iObj)

    def notify(self):
        for i in self.list:
            i.getNotification(i,self.highest_bid)

    def bidding(self):
        self.highest_bid += 200
        self.notify()


class Iobj(ABC):
    @abstractmethod
    def getNotification(self):
        pass

class Bidder1(Iobj):

    def getNotification(self, current_bid):
        print(current_bid)


class Bidder2(Iobj):

    def getNotification(self, current_bid):
        print(current_bid)


class Bidder3(Iobj):

    def getNotification(self, current_bid):
        print(current_bid)

b1=Bidder1
b2=Bidder2
b3=Bidder3
y=Auctioner(200)
y.subscribe(b1)
y.subscribe(b2)
y.subscribe(b3)
y.bidding()
