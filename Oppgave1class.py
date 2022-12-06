import csv      #Jeg begynner med å importere csvleser


def csvfil():       #Lager en funksjon for å lese csv filen
    file = open("adresser.csv", "r")        #Åpner csv fil og bruker utf-8
    data = list(csv.reader(file, delimiter=","))        #Leser gjennom filen med komma som seperator
    file.close()        #Lukker csv filen
    return data     #Returnerer daten som har blitt hentet

def txtfil():
    with open('adresser.txt') as f:
        txt = f.readlines()
        return txt




class Adresseliste:
    def __init__(self, søk=0):
        self.søk = søk
        self.bib = {"Navn": [], "Adresse": [], "Postnummer": []}

    def lagliste(self):
        pers = []
        liste = []
        for i in range(0, len(txtfil())):
            if len(txtfil()[i]) == 1:
                liste.append(pers)
                pers = []
            else:
                pers.append(txtfil()[i])
        
        for i in range(0, len(csvfil())):
            liste.append(csvfil()[i])

        return(liste)
    
    def sorter(self):
        l1 = Adresseliste()
        for i in range(0, len(l1.lagliste())):
            self.bib["Navn"].append(l1.lagliste()[i][0])
            self.bib["Adresse"].append(l1.lagliste()[i][1])
            self.bib["Postnummer"].append(l1.lagliste()[i][2])
        print(self.bib)
        return(self.bib)


    def sok(self):
        s1 = Adresseliste()
        teller = 0
        navneliste = s1.sorter()["Navn"]
        gateliste = s1.sorter()["Adresse"]
        postnummerliste = s1.sorter()["Postnummer"]
        lengde = len(navneliste)/3

        for i in range(0, int(lengde)):
            if self.søk in postnummerliste[i]:
                print(f"Postnummer funnet\nAdresse: {gateliste[i]}Postnummer: {postnummerliste[i]}")
                teller = teller +1

            elif self.søk in navneliste[i]:
                print(f"Navn funnet\n{navneliste[i]}Bor i {gateliste[i]}")
                teller = teller +1
            
            elif self.søk in gateliste[i]:
                print(f"Gate funnet\n{gateliste[i]}Tilhører {navneliste[i]}")
                teller = teller +1

        if teller == 0:
            print("Ingen på Adresselisten har dette Navnet/adressen/postnummeret")
        
l1 = Adresseliste()
print("Lengden av adresselisten er ", len(l1.lagliste()))
søk = str(input("Hva eller hvem vil du finne i adresselisten? \n>> "))
søker = Adresseliste(søk)
søker.sok()