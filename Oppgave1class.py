import csv      #Jeg begynner med å importere csvleser
import collections


def csvfil():       #Lager en funksjon for å lese csv filen
    file = open("adresser.csv", "r")        #Åpner csv fil og bruker utf-8
    data = list(csv.reader(file, delimiter=","))        #Leser gjennom filen med komma som seperator
    file.close()        #Lukker csv filen
    return data     #Returnerer daten som har blitt hentet

def txtfil():       #Lager en funskjon for å lese txt filen
    with open('adresser.txt') as f:         #Åpner txt filen
        txt = f.readlines()         #Leser txt filen
        return txt          #Returnerer datean fra txt filen




class Adresseliste:         #Oppretter klassen for adresselisten
    def __init__(self, søk=0):          #Legger til krav
        self.søk = søk          
        self.bib = {"Navn": [], "Adresse": [], "Postnummer": []}            #Defienerer et dictionary som skal inneholde navn, adresse og postnummer

    def lagliste(self):         #Lager en egenskap til classen. Skal ordne dataen slik at den leses likt
        pers = []              
        liste = []          #Definerer to lister
        for i in range(0, len(txtfil())):           #Går gjennom txt filen i en løkke og appender i "liste"
            if len(txtfil()[i]) == 1:
                liste.append(pers)
                pers = []
            else:
                pers.append(txtfil()[i])
        
        for i in range(0, len(csvfil())):       #Går gjennom csv filen i en løkke og appender i "liste"
            liste.append(csvfil()[i])
        
        self.fjern = [item for item, count in collections.Counter(liste).items() if count > 1]      #Finner likheter...
        liste.remove(self.fjern)        #...og fjerner de

        return(liste)           #Returnerer all dataen i en liste

    def sorter(self):           #Lager en ny egenskap som sorterer listen i Navn, Adresse og Poststed
        l1 = Adresseliste()
        for i in range(0, len(l1.lagliste())):      #Kjører gjennom en løkke og plasserer all dataen i riktig kategori
            self.bib["Navn"].append(l1.lagliste()[i][0])
            self.bib["Adresse"].append(l1.lagliste()[i][1])
            self.bib["Postnummer"].append(l1.lagliste()[i][2])

        return(self.bib)            #Returnerer biblioteket med all dataen


    def søk(self):      #Lager en funksjon for å søke etter informasjon
        s1 = Adresseliste()
        teller = 0
        navneliste = s1.sorter()["Navn"]        
        gateliste = s1.sorter()["Adresse"]
        postnummerliste = s1.sorter()["Postnummer"]
        lengde = len(navneliste)/3

        for i in range(0, int(lengde)):         #Løkker gjennom listen med adresser og finner frem navn, adresser og/eller postnummer som passer med ditt søk
            if self.søk in postnummerliste[i]:
                print(f"Postnummer funnet\nAdresse: {gateliste[i]}Postnummer: {postnummerliste[i]}")
                teller = teller +1

            elif self.søk in navneliste[i]:
                print(f"Navn funnet\n{navneliste[i]}Bor i {gateliste[i]}")
                teller = teller +1
            
            elif self.søk in gateliste[i]:
                print(f"Gate funnet\n{gateliste[i]}Tilhører {navneliste[i]}")
                teller = teller +1

        if teller == 0:         #Sier i fra om søket ikke er i listen
            print("Ingen på Adresselisten har dette Navnet/adressen/postnummeret")

        print("Gjenngående adresser", self.fjern)       #Printer hvem som er like i listene
        
l1 = Adresseliste()             #Aktiverer klassen og printer ut lengden av adresselisten
print("Lengden av adresselisten er ", len(l1.lagliste()))
søk = str(input("Hva eller hvem vil du finne i adresselisten? \n>> "))      #Aktiverer søk
søker = Adresseliste(søk)
søker.søk()