import random

def hodkostkou(strany=6):
    return random.randint(1, strany)

class Hrac:

    def __init__(self, profese, ziskanasila, ziskanemagy):
        self.profese = profese
        if profese == "Hranicarka":
            startsila = 5
            startmagy = 2
            self.pohlavi = "f"
        else:
            startsila = 4
            startmagy = 4
            self.pohlavi = "m"
        self.ubranezivoty = 0
        self.vycerpanemagy = 0
        self.zkusenost = 3
        self.zlataky = 3
        self.maxzivoty = startsila + ziskanasila
        self.zivoty = startsila + ziskanasila - self.ubranezivoty
        self.sila = self.zivoty
        self.maxvule = startmagy + ziskanemagy
        self.vule = startmagy + ziskanemagy - self.vycerpanemagy
        self.zivy = True

        def predstav_se(self):
           return f"Jsem {self.profese}, mam {self.startsila} zivotu a {self.startvule} magu"
   

