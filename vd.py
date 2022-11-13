class Uczen:
    matematyka= []
    informatyka= []
    historia= []

    def __init__(self, imie ,nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    def srednia(self):
        suma=0
        for i in self.matematyka:
            suma+=i
        return suma/len(self.matematyka)
    def najwiekszaocena(self):
        return max(matematyka)
    def informacje(self):
        print("oceny z matematyki:", uczen1.matematyka)
        print(uczen1)
        print("oceny z informatyki;",uczen1.informatyka)
        print("oceny z historii:",uczen1.historia)
uczen1 = Uczen("Jan", "Kowalski")
uczen1.matematyka=[1,2,3,4,5]
uczen1.informatyka=[3,4,4,3,5]
uczen1.historia=[5,5,5,4,3]
uczen1.informacje()