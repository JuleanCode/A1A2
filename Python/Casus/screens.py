import screenCompo
from menuLink import *
import datacheck
import req

import pyttsx3
import gtts
from playsound import playsound
import sys
import random
import time

# main menu for the user
def mainMenu():
    screenCompo.clear_screen()
    screenCompo.title()
    print("_____Hoofdmenu_____")
    #creates a menu for the user 
    screenCompo.menu_generator([MenuLink("Uitleg", explanation), MenuLink("Oefenen", learn), MenuLink("Score", score), MenuLink("Afsluiten", stop)])

# a page with a overview of al the 7 C's
def explanation():
    screenCompo.clear_screen()
    screenCompo.title()
    print("_____Uitleg:_____")

    sevenC = req.get_C()

    # to make the menu to select one of the 7 C's
    i = 1
    for C in sevenC:
        print(f"{i}) {sevenC[C]}")
        i += 1
    print(f"{i}) Terug")

    input_valid = False
    user_in = ""
    while not input_valid:
        user_in = input("=>")
        if user_in == str(i):
            input_valid = True
        # to check if the input exist in de dict
        elif user_in not in sevenC:
            print("Voer een juist getal in.")
        else:
            input_valid = True
            read(sevenC[user_in])

# the page to explain one of the C's
def read(data):
    screenCompo.clear_screen()
    screenCompo.title()
    print("_____Uitleg:_____")

    info = req.info_C()
    print(data)
    print(info[data])

    # to start the (gtts) text to speech engine (almost every language)
    #tts = gtts.gTTS(info[data], lang="nl")
    #tts.save(f"assets/{data}.mp3")
    playsound(f"assets/{data}.mp3")

    # to start the (pyttsx3) text to speech engine (only English)
    #\engine = pyttsx3.init()
    #engine.say(info[data])
    #engine.runAndWait()

    print("\nDruk op enter om terug te gaan.")
    input("=>")

# a page where the student can learn with the 7 C's
def learn():
    screenCompo.clear_screen()
    screenCompo.title()
    print("_____Oefenen:_____")

    info = req.info_C()

    # to gat a randomized dict 
    infoKeys = list()
    for i in info.keys():
        infoKeys.append(i)

    newInfo = dict()
    i = 0
    while i < len(info):
        # time.sleep() because random is not really random
        time.sleep(0.05)
        key = random.choice(infoKeys)
        if key not in newInfo:
            newInfo[key] = info[key]
            i += 1
    
    # to load every question
    score = 0
    for i in newInfo:
        screenCompo.clear_screen()
        screenCompo.title()
        print("_____Oefenen:_____")

        print(newInfo[i])
        playsound(f"assets/{i}.mp3")
        
        print("Welke van de 7 C's is dit? (type terug om terug te gaan naar het hoofdmenu)")
        start = time.time()
        user_in = input("=>")
        
        done = time.time()
        if user_in == i or user_in == i.lower() or user_in == i.upper():
            elapsed = done - start
            elapsed = int(elapsed)
            # the score is based on how quick the use gives the correct awnser 
            if elapsed < 60:
                score += 60 - elapsed
            print("Het antwoord is juist")
            time.sleep(5)
        elif user_in == "terug":
            #to go back to the homemenu
            mainMenu()
        else:
            print(f"Het antwoord is niet juist. Het goede antwoord was ({i})")
            time.sleep(5)
    
    # getting the name from the user to save later in the database
    input_valid = False
    user_in = ""
    while not input_valid:
        print("Wat is uw naam")
        user_in = input("=>")
        # check if user_in is all alphabetic characters (letters)
        if user_in.isalpha():
            input_valid = True
            userName = user_in
        else:
            print("Er ging iets mis voer uw naam opnieuw in.")
    
    print(f"De score van {userName} is {score}")
    time.sleep(10)

    req.save_score(userName, score)

# displays the top 5 scores
def score():
    screenCompo.clear_screen()
    screenCompo.title()
    print("_____Top 5 scores:_____")

    # gets the top 5 scores from de database
    score = req.get_score()

    for i in score:
        print(i)

    print("\nDruk op enter om terug te gaan.")
    input("=>")

# this function is used to close the application 
def stop():
    screenCompo.clear_screen()
    print("Tot ziens!")
    time.sleep(5)

    sys.exit()