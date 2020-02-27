from Strategy import Payment
class Shopping():
    def pay(self,x):
        x.execute()

s=Shopping()
b =Payment.Bkash()
s.pay(b)