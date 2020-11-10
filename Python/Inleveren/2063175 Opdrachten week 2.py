som = 0
i = 0

while i < 12:
    print(i)
    som += i
    i += 1


som = 0

for i in range(0, 12):
    print(i)
    som += i


hexWaarde = input("Geef de hexadecimale waarde:")
grondtal = 16
macht = 1
result = 0

while hexWaarde != "":
    cijfer = hexWaarde[-1]
    hexWaarde = hexWaarde[:-1]

    waarde = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
    '8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}[cijfer]
    
    result = result + waarde * macht
    macht = macht * grondtal

print(result)

#-------------------------------------------------------------------------------
# Opdracht 1:
#
# Invoer : een geheel getal
# Uitvoer: als de invoerstring foutieve tekens bevat:
#               "de invoer bevat foutieve tekens"
#          a. het getal in omgekeerde volgorde
#          b. de som van de cijfers
# Let op:  Geen gebruik van isdigit() of isnumeric() functies! 
#	   Tevens mag er geen gebruik worden gemaakt van de try except!
#-------------------------------------------------------------------------------

getal = input("Voer een nummer in:")
key = True

for nummer in getal:
    if nummer not in ['1','2','3','4','5','6','7','8','9','0']:
        print("de invoer bevat foutieve tekens")
        key = False

if key: #== True:
    print(getal[::-1])

    uitkomst = int(0)
    for nummer in getal:
        uitkomst += int(nummer)

    print(uitkomst)

#-------------------------------------------------------------------------------
# Opdracht 2:
#
# Invoer : een geheel getal
# Uitvoer: als de invoerstring foutieve tekens bevat:
#               "de invoer bevat foutieve tekens"
#          het aantal oneven cijfers, het aantal even cijfers
# Let op:  Geen gebruik van isdigit() of isnueric()!
#	   Tevens mag er geen gebruik worden gemaakt van de try except!
#-------------------------------------------------------------------------------

getal = input("Voer een nummer in:")
key = True

for nummer in getal:
    if nummer not in ['1','2','3','4','5','6','7','8','9','0']:
        print("de invoer bevat foutieve tekens")
        key = False

if key:
    even = 0
    oneven = 0
    for nummer in getal:
        if nummer in ['2','4','6','8','0']:
            even += 1
        else:
            oneven += 1
    
    print(f"er zijn {even} getallen")
    print(f"er zijn {oneven} getallen")

#-------------------------------------------------------------------------------
# Opdracht 3:
#
# Invoer : een (lange) string 'zin' en een integer 'getal'
# Uivoer : de string zin in kleine letters, maar elke getal-de karakter als
#          hoofdletter
# Bv. invoer:
#     zin = "Een (Lange) String S En Een Cijfer N"
#     getal = 4
#     uitvoer: "een (laNge) strIng S en een cijFer N"
#
#-------------------------------------------------------------------------------

zin = input("Vul een zin in")
getal = int(input("vul een getal in"))
teller = getal
nieuweZin = ""

for letter in zin:
    if teller < 1:
        nieuweZin += letter.upper()
        teller = getal
    else:
        nieuweZin += letter.lower()
        teller -= 1

print(nieuweZin)

#-------------------------------------------------------------------------------
# Opdracht 4:
#
# Invoer : een (lange) string 'zin'
# Uivoer : de string zin in camelCase (zonder spaties elke 2de letter vanaf het
#          tweede woord als hoofdletter)
# Bv. invoer:
#     zin = "een STRING s en een cijfer n"
#     uitvoer: "eensTringseNeEncIjfern"
# Let op:  Geen gebruik maken van: .title(), .join() en map() functies!
#-------------------------------------------------------------------------------

zin = input("Vul een zin in").lower()
nieuweZin = ""

#Teller staat op 2 omdat de loop anders al start
teller = 2

for letter in zin:
    if letter is " ": #kijkt of er een spatie
        teller = 0
    elif teller == 1:
        nieuweZin += letter.upper()
        teller = teller + 1
    else:
        nieuweZin += letter
        teller = teller + 1

print(nieuweZin)

#-------------------------------------------------------------------------------
# Opdracht 5:
#
# Invoer : een (lange) string 'zin'
# Uivoer : de string zin met na elk teken een spatie
# Bv. invoer:
#     zin = "een string s en een cijfer n"
#     uitvoer: "e e n   s t r i n g   s   e n   e e n   c i j f  e r   n "
# Let op:  Er mogen GEEN string-functions toegepast worden.
#          Geen gebruik van .title(), .join() en map functies
#-------------------------------------------------------------------------------

zin = input("Vul een zin in")
nieuweZin = ""

for letter in zin:
    nieuweZin += letter + " "

print(nieuweZin)

#-------------------------------------------------------------------------------
# Opdracht 6:
#
# Invoer : een positief geheel getal (getal > 0)
# Uivoer : de rij van Collatz
# De termen van de rij van Collatz worden als volgt berekend:
# Start met getal=,
#     als getal == 1: dan stopt de rij
#     als getal is even getal // 2
#     als getal is oneven getal * 3 + 1
# Invoer : 13
# Uitvoer: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
#
#-------------------------------------------------------------------------------

getal = int(input("Voer een geheel getal in"))
print(getal)

while getal > 1:
    if (getal % 2) == 0:
        getal = getal // 2
        print(getal)
    else:
        getal = getal * 3 + 1
        print(getal)