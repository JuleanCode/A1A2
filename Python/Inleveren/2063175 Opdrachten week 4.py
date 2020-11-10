
def SterrenToevoegen(tekst1, tekst2):

    tekst3 = tekst2 + tekst1 + tekst2
    return(tekst3)

tekst1 = input()
tekst2 = "***"
print(SterrenToevoegen(tekst1, tekst2))

#-------------------------------------------------------------------------------
# Name:        Opdrachten week 4
# Purpose:
#
# Author:      Bour / Zegers / Tossaint
#
# Created:     20-02-2016
# Changed:     14-01-2020
#-------------------------------------------------------------------------------
'''
Deze week worden de opdrachten door middel van een function uitgevoerd. De 
gegevens worden aan de function doorgegeven via parameters. De resultaten
worden als returnwaarde terug gegeven.
'''
#-------------------------------------------------------------------------------
# Opdracht 1:
#
# Invoer : Twee lijsten met gehele getallen
# Uitvoer: De getallen, die beide lijsten gemeenschappelijk hebben.
# Let op: maak gebruik van functies EN parameters EN locale variabelen
#         gebruik van de set() functie is hierbij niet toegestaan!
#         Maak dus gebruik van de kennis opgedaan in de lessen!
#-------------------------------------------------------------------------------

def check(invoer1, invoer2):
    gelijkeNummers = ""

    for i in invoer1:
        if i in invoer2 and i not in gelijkeNummers:
            gelijkeNummers += i

    return(gelijkeNummers)

invoer1 = input("Geef een lijst met gehele getallen op")
invoer2 = input("Geef een lijst met gehele getallen op")

print("Deze nummers kommen in bijde lijsten voor " + check(invoer1, invoer2))

#-------------------------------------------------------------------------------
# Opdracht 2:
#
# Invoer : Twee lijsten (A en B) met gehele getallen
# Uitvoer: De getallen, die in lijst A voorkomen en NIET in lijst B.
# Let op: maak gebruik van functies EN parameters EN locale variabelen
#         gebruik van de set() functie is hierbij niet toegestaan
#         Maak dus gebruik van de kennis opgedaan in de lessen!
#-------------------------------------------------------------------------------

def check(A, B):
    nietGelijkeNummers = ""

    for i in A:
        if i not in B:
            nietGelijkeNummers += i

    return(nietGelijkeNummers)

A = input("Geef een lijst met gehele getallen op")
B = input("Geef een lijst met gehele getallen op")

print("Deze nummers kommen alleen in lijst A voor " + check(A, B))

#-------------------------------------------------------------------------------
# Opdracht 3:
#
# Invoer : Twee lijsten (A en B) met gehele getallen
# Uitvoer: Een antwoord op de vraag of alle getallen van lijst A in lijst B
#          voorkomen of alle getallen van lijst B in lijst A
# Let op: maak gebruik van functies EN parameters EN locale variabelen
#         gebruik van de set() functie is hierbij niet toegestaan
#         Maak dus gebruik van de kennis opgedaan in de lessen!
#-------------------------------------------------------------------------------

def check1(A, B):
    isGelijk = "wel"

    for i in A:
        if i not in B:
            isGelijk = "niet"

    return(isGelijk)

def check2(A, B):
    isGelijk = "wel"

    for i in A:
        if i not in B:
            isGelijk = "niet"

    return(isGelijk)

A = input("Geef een lijst met gehele getallen op")
B = input("Geef een lijst met gehele getallen op")

print("Alle getallen van lijst A komen " + check1(A, B) + " voor in lijst B")
print("Alle getallen van lijst B komen " + check2(A, B) + " voor in lijst A")

#-------------------------------------------------------------------------------
# Opdracht 4:
#
# Invoer : Twee lijsten (A en B) met gehele getallen
# Uitvoer: Een lijst C, waarin alle getallen van de lijsten A en B slechts
#          1 keer voorkomen.
# Let op: maak gebruik van functies EN parameters EN locale variabelen
#         gebruik van de set() functie is hierbij niet toegestaan
#         Maak dus gebruik van de kennis opgedaan in de lessen!
#-------------------------------------------------------------------------------

def check(A, B):
    C = []

    for i in A:
        if i not in C:
            C.append(i)

    for i in B:
        if i not in C:
            C.append(i)

    return(C)

A = input("Geef een lijst met gehele getallen op")
B = input("Geef een lijst met gehele getallen op")

print("Dit zijn alle waardes die voorkomen in lijst A en B " + check(A, B))

#-------------------------------------------------------------------------------
# Opdracht 5:
# In een dictionary wordt per "regel" een zogenaamd "keyValuePair" opgenomen.
# in deze opgave wordt gebruik gemaakt van een dictionary, die er als volgt uit
# ziet:
# key: naam
# value: [naam, geboortedatum, mail-adres]
# Maak functies voor het raadplegen, toevoegen, verwijderen en wijzigen in de
# dictionairy:
# data: {'Jan':['Jansen','10-10-2000','mail@mail.com'], 
#        'Rob':['Frissen','13-08-1997','mail1@mail.com'],
#        'Ida':['Klaasen','23-03-1949','mail2@mail.com']}
# Invoer : functietype ('r', 't', 'v', of 'w') en bij ('t', 'v', of 'w') de
#          gegevens om de functie uit te voeren.
# Uitvoer: Een overzicht van de gegevens in een goed leesbare tabel ('r').
# Let op:  Start het programma met het vullen van een dictionairy met
#          bovenstaande data.
#          Zorg voor de juiste controles bij het toevoegen en wijzigen!!
#          Dus bestaat een key al dan bij toevoegen dan een gepaste melding
#          vraag vervolgens of de invoerder het record wil wijzigen!
#-------------------------------------------------------------------------------

import os       #Voor de clear screen functie
import time     #Voor de sleep functie
#import yaml     #moet nog geinstaleerd worden


data = {'Jan':['Jansen','10-10-2000','mail@mail.com'], 
        'Rob':['Frissen','13-08-1997','mail1@mail.com'],
        'Ida':['Klaasen','23-03-1949','mail2@mail.com']}

def menu():
    check = True

    while check:
        print(" 1.   toevoegen\n", 
            "2.   overzicht\n", 
            "3.   aanpassen\n", 
            "4.   verwijderen\n")

        try:
            invoer = int(input(":"))
            check = False
        except ValueError:
            print("U moet een nummer invoeren")
            
            time.sleep(3.5)
            clearScreen()
    
    screens(invoer)


def mainScreen():
    clearScreen()

    menu()

def screens(screen):
    clearScreen()

    if screen == 1:     #create
        print(read())
        
        create()

    elif screen == 2:   #read
        print(read())

        menu()

    elif screen == 3:   #update
        print(read())
        
        update()

    elif screen == 4:   #delete
        print(read())
        
        delete()

def clearScreen():
    os.system('cls')


#CRUD systeem

def create():
    check = True

    while check:
        fName = input("Voornaam: ")
        lName = input("Achternaam: ")
        date = input("Geboorte datum: ")
        email = input("E-mail: ")

        if fName not in data:
            newUser = {}
            newUser[fName] = [lName, date, email]

            data.update(newUser)

            check = False
        else:
            print("user bestaat al in de lijst")

            time.sleep(3.5)
    
def read():
    return(data)

def update():

    check = True

    while check:
        fName = input("Voornaam: ")
        lName = input("Achternaam: ")
        date = input("Geboorte datum: ")
        email = input("E-mail: ")

        if fName in data:
            updateUser = {}
            updateUser[fName] = [lName, date, email]

            data.update(updateUser)

            check = False
        else:
            print("user bestaat niet in de lijst")

            time.sleep(3.5)

def delete():

    check = True

    while check:
        print("Welke gebruiker wilt u verwijderen?")

        fName = input("Voornaam: ")

        if fName in data:
            del data[fName]

            check = False
        else:
            print("user bestaat niet in de lijst")

            time.sleep(3.5)
    
while True:
    mainScreen()