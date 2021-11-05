import random

def hodkostkou(strany=6):
    return random.randint(1, strany)


#Snazne vas prosim, ignorujte zybtecnosti a nedokoncene veci. Zkousim si prevest do Pythonu co nejvice z deskove hry Proroctvi. Pokud ji neznate, tak vam asi souboj bude pripadat moc slozity, ale je podle pravidel.



#Hraci = []
#vecnaloviste = []
#lesnitabor = []
#gilda = []

class Hrac:

    def __init__(self, profese, ziskanasila, ziskanemagy):
        self.profese = profese
        if profese == "Hranicar":         
            startsila = 5
            startmagy = 2
            self.pohlavi = "m"
        elif profese == "Druid":            
            startsila = 3
            startmagy = 6
            self.pohlavi = "m"
        self.ubranezivoty = 0
        self.vycerpanemagy = 0
        self.zkusenost = 3
        self.zlataky = 3
        #self.pole = pole
        self.maxzivoty = startsila + ziskanasila
        self.zivoty = startsila + ziskanasila - self.ubranezivoty
        self.sila = self.zivoty
        self.maxvule = startmagy + ziskanemagy
        self.vule = startmagy + ziskanemagy - self.vycerpanemagy
        self.zivy = True

        print("Jsem " + self.profese + " a mam ", end = "")
        print(self.sila, end = "")
        print(" zivotu a ", end = "")
        print(self.vule, end = "")
        print(" magu.")
   
    def __repr__(self):
      return self.profese



class nestvura:
    def __init__(self, jmeno, druh, expy, silaprotif, silaprotim, vuleprotif, vuleprotim, zivoty=1):
        self.jmeno = jmeno
        self.druh = druh
        self.zkusenost = expy
        self.silaprotim = silaprotim
        self.silaprotif = silaprotif
        self.vuleprotim = vuleprotim
        self.vuleprotif = vuleprotif
        self.zivoty = zivoty
        self.zivy = True

def bojsnestvurou (co, koho):
    print(koho.profese + "narazil/a na nestvuru. Vypada jako " + co.jmeno +"! Nema na vybranou, jde se bojovat.")
    bylsoubojvuli = False
    while co.zivy == True and koho.zivy == True: 
        if koho.pohlavi == "f":
            #souboj Silou
            if co.silaprotif < 0 and ((koho.vule - 2) - co.vuleprotif)<=(koho.sila - co.silaprotif):
                if (koho.sila + (hodkostkou())) > (co.silaprotif + (hodkostkou())):
                    co.zivoty = co.zivoty -1
                    if co.zivoty == 0:
                        print(koho.profese + "zabila nestvuru známou jako " + co.jmeno + " a ziskala ", end="")
                        print(co.zkusenost, end="")
                        print(" expu.")
                    else:
                        print("Jeden zivot dole, jen tak dal!")
                elif (koho.sila + (hodkostkou())) == (co.silaprotif + (hodkostkou())):
                    print("Je to remiza!")
                    break
                elif (koho.sila + (hodkostkou())) < (co.silaprotif +(hodkostkou())):
                    print("Nestvura vyhrala. " + koho.profese + "ztraci jeden zivot.")
                    koho.ubranezivoty = koho.ubranezivoty +1
                    if koho.zivoty == 0:
                        print(self.profese + " precenila sve sily. Budeme na tebe vzpominat.")
                        koho.zivy = False
                        break
            #souboj vuli
            elif co.silaprotif == 0 or (koho.vule - 2) > co.vuleprotif:
                if bylsoubojvuli == False and co.silaprotif > 0:
                    koho.vycerpanemagy = koho.vycerpanemagy +2
                    bylsoubojvuli = True
                else:
                    break
                if (koho.vule + (hodkostkou())) > (co.vuleprotif + (hodkostkou())):
                    co.zivoty = co.zivoty -1
                    if co.zivoty == 0:
                        print(koho.profese + "zabila nestvuru známou jako " + co.jmeno + " a ziskala ", end="")
                        print(co.zkusenost, end="")
                        print(" expu.")
                    else:
                        print("Jeden zivot dole, jen tak dal!")
                elif (koho.vule + (hodkostkou())) == (co.vuleprotif + (hodkostkou())):
                    print("Je to remiza!")
                    break
                elif (koho.vule + (hodkostkou())) < (co.vuleprotif +(hodkostkou())):
                    print("Nestvura vyhrala. " + koho.profese + "ztraci jeden zivot.")
                    koho.ubranezivoty = koho.ubranezivoty +1
                    if koho.zivoty == 0:
                        print(self.profese + " precenila sve sily. Budeme na tebe vzpominat.")
                        koho.zivy = False
                        break
        else:
            #souboj Silou
            if co.silaprotim < 0 and ((koho.vule - 2) - co.vuleprotim)<=(koho.sila - co.silaprotim):
                if (koho.sila + (hodkostkou())) > (co.silaprotim + (hodkostkou())):
                    co.zivoty = co.zivoty -1
                    if co.zivoty == 0:
                        print(koho.profese + "zabila nestvuru známou jako " + co.jmeno + " a ziskala ", end="")
                        print(co.zkusenost, end="")
                        print(" expu.")
                    else:
                        print("Jeden zivot dole, jen tak dal!")
                elif (koho.sila + (hodkostkou())) == (co.silaprotim + (hodkostkou())):
                    print("Je to remiza!")
                    break
                elif (koho.sila + (hodkostkou())) < (co.silaprotim +(hodkostkou())):
                    print("Nestvura vyhrala. " + koho.profese + "ztraci jeden zivot.")
                    koho.ubranezivoty = koho.ubranezivoty +1
                    if koho.zivoty == 0:
                        print(self.profese + " precenila sve sily. Budeme na tebe vzpominat.")
                        koho.zivy = False
                        break
            #souboj vuli
            elif co.silaprotim == 0 or (koho.vule - 2) > co.vuleprotim:
                if bylsoubojvuli == False and co.silaprotim > 0:
                    koho.vycerpanemagy = koho.vycerpanemagy +2
                    bylsoubojvuli = True
                else:
                    break
                if (koho.vule + (hodkostkou())) > (co.vuleprotim + (hodkostkou())):
                    co.zivoty = co.zivoty -1
                    if co.zivoty == 0:
                        print(koho.profese + "zabila nestvuru známou jako " + co.jmeno + " a ziskala ", end="")
                        print(co.zkusenost, end="")
                        print(" expu.")
                    else:
                        print("Jeden zivot dole, jen tak dal!")
                elif (koho.vule + (hodkostkou())) == (co.vuleprotim + (hodkostkou())):
                    print("Je to remiza!")
                    break
                elif (koho.vule + (hodkostkou())) < (co.vuleprotim +(hodkostkou())):
                    print("Nestvura vyhrala. " + koho.profese + "ztraci jeden zivot.")
                    koho.ubranezivoty = koho.ubranezivoty +1
                    if koho.zivoty == 0:
                        print(self.profese + " precenila sve sily. Budeme na tebe vzpominat.")
                        koho.zivy = False
                        break
                    
                        
                    
                        
Loupeznik = nestvura("Loupeznik", "humanoid", 2, 3, 3, 3, 3)     
Inkubus = nestvura("Inkubus", "demon", 2, 0, 0, 5, 3)

Jamie = Hrac("Hranicar", 0, 0)
bojsnestvurou(Loupeznik,Jamie)



