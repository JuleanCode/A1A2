#-------------------------------------------------------------------------------
# Opdracht 1:
#
# Invoer : twee variabelen 'Inlognaam' en 'wachtwoord' (beide als string)
# Uitvoer: "Welkom <Inlognaam> bij de module Scripting." 
#		bij <Inlognaam> de ingevoerde naam weergeven!
# Hint	 : Zoek op internet naar 'strings aan elkaar koppelen in python'
#
#-------------------------------------------------------------------------------

from getpass import getpass

Inlognaam = input("Inlognaam: ")
Wachtwoord = getpass()

#Gebruik maken van f strings hiermee kunt je de waarde in {} zetten
print (f'Hallo {Inlognaam}')

#-------------------------------------------------------------------------------
# Opdracht 2:
#
# Invoer : twee variabelen 'getala' en 'getalb' (als integer)
# Uitvoer: de tekst "<getala> tot de macht <getalb> is: " getala^getalb
#          op de plek <getala> en <getalb> de waarde tonen van die variabelen!!
# Hint   : Zorg dat de cijfers door python als getal worden gezien
#          zoek hiervoor op internet de geschikte functie of zie hoorcollege
#          week 1.
#-------------------------------------------------------------------------------

Getala = int(input("Geeft getal 1: "))
Getalb = int(input("Geeft getal 2: "))
Getalc = (Getala ** Getalb)

print (f'{Getala} tot de macht {Getalb} is {Getalc}')

#-------------------------------------------------------------------------------
# Opdracht 3:
#
# Invoer : een geheel getal 'getala' (als integer)
# Uitvoer: een rechthoek met de lengte 'getala' (horizontaal) en de breedte 3 regels
#          (verticaal). De lijnen worden weergegeven als ster (*).
# voorbeeld:
#           bij waarde <getala> = 5
#               *****
#               *****
#               *****
# Hint   : Zoek op internet hoe je hiervoor de print() functie kunt gebruiken!
#-------------------------------------------------------------------------------

Getala = int(input("Hoeveel * wilt u op het beeld: "))
i = 1

while i < 4:
    print(Getala * "*")
    i += 1

#-------------------------------------------------------------------------------
# Opdracht 4:
#
# Invoer : n.v.t.
# Uitvoer: het decimale getal 100 in binaire, octale en hexadecimale weergave
#	   weergeven
# Hint   : Gebruik internet om mogelijke oplossingen hiervoor te vinden!
#-------------------------------------------------------------------------------

dec = 100

print (bin(dec))
print (oct(dec))
print (hex(dec))

#-------------------------------------------------------------------------------

# Opdracht 5:
#
# Invoer : n.v.t.
# Uitvoer: decimale waarde weergeven van het binaire getal 100
#          decimale waarde weergeven van het octale getal 100
#          decimale waarde weergeven van het hexadecimale getal 100
#-------------------------------------------------------------------------------

dec = 100

bin = (bin(dec))
oct = (oct(dec))
hex = (hex(dec))

print (int(bin, 2))
print (int(oct, 8))
print (int(hex, 16))

#-------------------------------------------------------------------------------
# Opdracht 6:
#
# Invoer : een variabele 'woord' (als string) en een variabele 'getal' (als integer)
# Uitvoer: getal * woord gescheiden door een " x "
# voorb	 : woord = 'boom' en getal = 6
#	   boom x boom x boom x boom x boom x boom
#-------------------------------------------------------------------------------

woord = input("Voer een woord in: ")
getal = int(input("Voer een getal in: "))

print ((getal-1) * (woord + " X ") + woord)

#-------------------------------------------------------------------------------
# Opdracht 7: 
#
# Invoer : een variabele 'woord' (als string) en een variabele 'getal' (als integer)
# Uitvoer: de eerste <getal> aantal karakters van woord en de laatste <getal> 
#          karakters van woord
# Hint   : Zoek op internet hoe je een substring kunt gebruiken binnen Python!
#          substring = deel van een string
#-------------------------------------------------------------------------------

woord = input("Voer een woord in: ")
getal = int(input("Voer een getal in: "))

print (woord[0:getal])
print (woord[-getal:])

