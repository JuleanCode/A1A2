
rij1 = [8, 15, 9, 44, 2, 7, 6, 2]
uitkomst = 0

for cijfer in rij1:
    uitkomst += cijfer

print(uitkomst)

print(sum(rij1))

#-------------------------------------------------------------------------------
# Opdracht 1:
#
# Invoer : -
# Uitvoer 1: Initialiseer een lijst met de getallen 1 t/m 10 en druk de lijst af.
# Uitvoer 2: Initialiseer een lijst met de getallen 1 t/m 10 en druk ieder item
#            in de lijst af op een nieuwe regel!
#-------------------------------------------------------------------------------

lijst = []

for getal in range(1, 11):
    lijst.append(getal)

print(lijst)

#-------------------------------------------------------------------------------
# Opdracht 2:
#
# Invoer : vraag een getal tussen de 0 en de 101.
# Uitvoer: Initialiseer een lijst met de getallen 1 t/m 100 en druk het
#          bij getal behorende element af.
#
#-------------------------------------------------------------------------------

invoer = int(input("Geef een getal tussen de 0 en de 101 op"))
lijst = []
i = 0
check = True

for getal in range(1, 101):
    lijst.append(getal)

for getal in lijst:
    if getal == invoer:
        print(f"Het getal {invoer} heeft als bijbehoorend element {i}")
        check = False
    else:
        i += 1

#-------------------------------------------------------------------------------
# Opdracht 3:
#
# Invoer : vraag twee getallen tussen de 0 en de 11.
# Uitvoer: Initialiseer een lijst met de getallen 1 t/m 10 en druk de som
#          van de waarde van de elementen in de lijst af.
#          voorbeeld 3 en 4, dan de som van het 3de en 4de element in de lijst
#          afdrukken 
#-------------------------------------------------------------------------------

invoer1 = int(input("Geef een getal tussen de 0 en de 11 op"))
invoer2 = int(input("Geef een getal tussen de 0 en de 11 op"))
lijst = []

for getal in range(1, 11):
    lijst.append(getal)

waarde1 = int(lijst[invoer1])
waarde2 = int(lijst[invoer2])

print(waarde1 + waarde2)

#-------------------------------------------------------------------------------
# Opdracht 4:
#
# Invoer : vraag twee getallen tussen de 0 en de 101.
# Uitvoer: Initialiseer een lijst met de getallen 1 t/m 100 en druk het product
#          van de waarde van de elementen in de lijst af.
#          voorbeeld 3 en 4, dan het product van het 3de en 4de element in de 
#          lijst afdrukken 
#-------------------------------------------------------------------------------

invoer1 = int(input("Geef een getal tussen de 0 en de 101 op"))
invoer2 = int(input("Geef een getal tussen de 0 en de 101 op"))
lijst = []

for getal in range(1, 101):
    lijst.append(getal)

waarde1 = int(lijst[invoer1])
waarde2 = int(lijst[invoer2])

print(waarde1 * waarde2)

#-------------------------------------------------------------------------------
# Opdracht 5:
#
# Invoer : -
# Uitvoer: Initialiseer een list met de getallen 1 t/m 5. Voeg aan deze list
#          een nieuwe list toe met de getallen 6 t/m 10.
#          druk eerste het 5de element af en 
#          druk vervolgens het getal 6 uit de lijst af
#-------------------------------------------------------------------------------

lijst1 = []
lijst2 = []

for getal in range(1, 6):
    lijst1.append(getal)

for getal in range(6, 11):
    lijst2.append(getal)

lijst3 = lijst2 + lijst1

print(lijst3[5])
print(lijst3[0])

#-------------------------------------------------------------------------------
# Opdracht 6:
#
# Invoer : -
# Uitvoer: Initialiseer een lijst met de getallen 1 t/m 5. Voeg aan deze lijst
#          een nieuwe lijst toe (lijst in een lijst) met de getallen 6 t/m 10.
#          (DUS NIET -> [1,2,3,4,5,6,7,8,9,10]) verander nu de waarde 6 in een 'A'
#          voeg vervolgens aan de lijst met de waarden ['A',7,8,9,10]
#          de waarde 11 toe. Druk vervolgens de gehele lijst af.
#-------------------------------------------------------------------------------

lijst1 = []
lijst2 = []

for getal in range(1, 6):
    lijst1.append(getal)

for getal in range(6, 11):
    lijst2.append(getal)

lijst1.append(lijst2)

lijst1[5][0] = 'A'
lijst1[5].append(11)

print(lijst1)

#-------------------------------------------------------------------------------
# Opdracht 7:
#
# Invoer : een positief geheel getala
# Uitvoer: Initialiseer een lijst met de getallen <getala> t/m 1 en
#          druk de lijst af.
#
#-------------------------------------------------------------------------------

invoer = int(input("Geef een positief geheel op"))
lijst = []

for getal in range(invoer, 0, -1):
    lijst.append(getal)

print(lijst)

#-------------------------------------------------------------------------------
# Opdracht 8:
#
# Invoer : een getala en een getalb
# Uitvoer: vul een lijst met de getallen vanaf a t/m b.
#          als b kleiner is dan a dan een lijst vanaf b t/m a
#          zijn de getallen evengroot dan een gepaste melding en opniew om
#          invoer vragen
#-------------------------------------------------------------------------------

lijst = []
invoer()

getala = ""
getalb = ""

def invoer():
    while getala == getalb:
        getala = int(input("vul een getal in"))
        getalb = int(input("vul een getal in"))
        
    aanmaak(getala, getalb)

def aanmaak(getala, getalb):                                                
    if getalb < getala:
        for getal in range(getalb, getala):
            lijst.append(getal)
    else:
        for getal in range(getala, getalb):
            lijst.append(getal)
    
    print(lijst)

#-------------------------------------------------------------------------------
# Opdracht 9:
#
# Invoer : een positief geheel getaln (> 0)
# Uitvoer: de rij van Fibonacci tot en met de n-de term
# De rij van Fibonacci is als volgt gedefinieerd:
#   F1 = 1
#   F2 = 1
#   F3 = 2  (= F1 + F2)
#   F4 = 3  (= F2 + F3)
#   F5 = 5  (= F3 + F4)
#   F6 = 8  (= F4 + F5)
#
#-------------------------------------------------------------------------------

invoer = int(input("Geef een positief geheel op"))                                      #TODO
getal1 = 0
getal2 = 1
check = 0

print(getal1)
getal2 += getal1

while check < invoer:
    if getal1 <= getal2:        #als getal1 kleiner of gelijk is aan getal2
        getal1 += getal2
        print(getal1)
    elif getal2 <= getal1:      #als getal2 kleiner of gelijk is aan getal1
        getal2 += getal1
        print(getal2)
    
    check += 1

#-------------------------------------------------------------------------------
# Opdracht 10:
#
# Invoer : een geheel getala en een geheel getalb
# Uitvoer: vul een lijst met de veelvouden van 10 van de getallen getala t/m getalb,
#          doe het vullen van de lijst in 1 regel code!
#-------------------------------------------------------------------------------

getala = int(input("voer een geheel getal in"))
getalb = int(input("voer een geheel getal in"))

lijst = [ i * 10 for i in range(getala, getalb)]

print(lijst)

#-------------------------------------------------------------------------------
# Opdracht 11:
#
# Invoer : breid het programma uit opdracht 10 uit door te controleren of de 
#          lijst meer dan 20 getallen bevat.
# Uitvoer: True of False
#-------------------------------------------------------------------------------

getala = int(input("voer een geheel getal in"))
getalb = int(input("voer een geheel getal in"))

lijst = [ i * 10 for i in range(getala, getalb)]

print(lijst)

if len(lijst) > 20:
    print("de lengte van de lijst is hoger dan 20")

#-------------------------------------------------------------------------------
# Opdracht 12:
#
# Invoer : vraag een getal van 10 cijfers
# Uitvoer: sla de cijfer individueel op in een lijst van getallen
#          maak gebruik van de for of while loop!
#          Leg m.b.v. een commentaarregel in je code uit waarom je voor de
#          for of de while hebt gekozen!
#          Gebruik van de list() functie is hierbij dus NIET toegestaan!
#-------------------------------------------------------------------------------

getal = input("Geef een getal van 10 cijfers op")

newGetal = []

for i in getal:
    newGetal.append(i)

print(newGetal)

#-------------------------------------------------------------------------------
# Opdracht 13:
#
# init   : gebruik de volgende dictionary
#          {'piet':'06-12345678','jan':'06-87654321'}
# Invoer : vraag een naam en een telefoonnummer
# Uitvoer: vul de bovenstaande dictionary aan met de ingevoerde gegeven,
#          print vervolgens de inhoud van de gehele dictionary af:
#          'Het Telefoonnummer van <naam> = <telefoonnummer>' 
#-------------------------------------------------------------------------------

users = {'piet':'06-12345678','jan':'06-87654321'}
newUser = {}

fName = input("Voornaam: ")
fNumber = input("Telefoonnummer: ")

newUser[fName] = fNumber
users.update(newUser)

for key, value in users.items():
    print(f"Het Telefoonnummer van {key} = {value}")

#-------------------------------------------------------------------------------
# Opdracht 14:
#
# Init:    Vul een dictionairy met als key de ascii-waarde en value de
#          bijbehorende character ('A' t/m 'Z') m.b.v. een for loop!
# Invoer : ascii-waarde asc
# Uitvoer: als asc in de dictionairy voorkomt de bijbehorende characterwaarde,
#          anders een gepaste melding.
#-------------------------------------------------------------------------------

import string

ascii_dict = dict()
ascii_in_number = range(ord('A'),ord('Z')+1)
for i in ascii_in_number:
    ascii_dict[chr(i)] = str(i)

invoer = input("voer de ascii waarde va een letter A-Z in")

for letter, asc in ascii_dict.items():
    if invoer == asc:
        print(f"de letter die bij de ascii waarde {asc} hoort is {letter}")

#-------------------------------------------------------------------------------
# Opdracht 15:
#
# Init     : Vul een dictionairy met als key de character-waarde ('A' t/m 'Z') en value de
#            bijbehorende ascii-waarde. m.b.v. een while loop!
# Invoer   : character waarde c
# Uitvoer a: alle characters en hun bijbehorende ascii-waarde in oplopende
#            volgorde
# Uitvoer b: alle characters en hun bijbehorende ascii-waarde in aflopende
#            volgorde
# Uitvoer c: als c in de dictionairy voorkomt de bijbehorende ascii-waarde,
#            anders een gepaste melding
#-------------------------------------------------------------------------------

letter = input("Give me a letter from A to Z: ")

asciiTable = {}

normalTable = ord("A")
reverseTable = ord("Z")

# ord() fumction returns an integer representing the Unicode character (A -Z)
# chr() function returns a character (a string) from an integer (represents unicode code point of the character)
#Initialises a dictionary from A to Z as keys and their corresponding ASCII number as value
while (normalTable != ord("Z") + 1):
    #Adds the corresponding number to the ASCII character
    asciiTable[chr(normalTable)] = normalTable
    normalTable += 1

#Print the ascending dictionary     
for i in asciiTable:
    print(i + " = " + str(asciiTable[i]))

print("\n")

#Initialise and print the descending dictionary
# -1 because going down from 90(Z) to 65(A) and to print A
while (reverseTable != (ord("A") - 1)):
    print(chr(reverseTable) + " = " + str(reverseTable))
    reverseTable -= 1

print("\n")

#Print the number if the given letter is in the dictionary
if letter in asciiTable:
    print(asciiTable[letter])
else:
    print("Silly, not a lowercase letter. Give me an uppercase letter!")
