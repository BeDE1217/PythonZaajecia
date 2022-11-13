import random
class Gra:
    obrazenia= random.randint(0,100)
    leczenie=[]
    exp=[]
    zdrowie=100
    statystyki=[]
    def __init__(self,exp):
        self.exp=exp
    def obrazenia(self):
        obrazenia= random.randint(0,100)
        for i in self.obrazenia:
            zdrowie=100-i
            return self.zdrowie
    def zdrowie(self):
        self.zdrowie=zdrowie
        zdrowie=100
    def leczenie(self):
        if zdrowie<=0:
            print('zginales')
    def exp(self):
        exp=0
        for i in random.randint(0,1000):
            exp+=i
        return exp(self.exp)
    def statystyki(self):
        statystyki=0
        for i in self.leczenie:
            statystyki+=i
        return statystyki(self.statystyki)

print("Witaj w grze: jak nazywa sie twój wojownik?")
gracz=Gra(input("Nazwa: "))
gracz.zdrowie=[100]
while (True):
    print("I  p- !start gry!     I")
    print("I s- statystki gracza I")
    print("I t-    exp           I")
    print("I x- wyjscie z gry    I")
    a= input("TWÓJ WYBÓR:")
    if a =='t':
        print(gracz.exp())
    if a=='x':
        break
    if a=='p':
        print(gracz.)





