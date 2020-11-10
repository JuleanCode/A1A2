import re
import platform
import os

import time
# contains different components for the screens

def title():
	print("""               _        _    _     _ 
              | |      | |  (_)   | |
  ___ ___   __| | ___  | | ___  __| |
 / __/ _ \ / _` |/ _ \ | |/ / |/ _` |
| (_| (_) | (_| |  __/ |   <| | (_| |
 \___\___/ \__,_|\___| |_|\_\_|\__,_|
                                     """)

def clear_screen():
	if platform.platform()[:7] == "Windows":
		os.system("cls")
	else:
		os.system("clear")

# 404 page when a link is not well defined
def error_404():
    clear_screen()
    title()
    print("_____kon deze pagina niet vinden._____")
    time.sleep(3)
    
# to make a menu for the user
# get's a list of options these options are links to different pages
def menu_generator(options):
    input_valid = False
    # in what range are the options
    range_options = len(options)
    i = 0
    # show the options on the screen
    for op in options:
        i += 1
        print(i, ") " + op.text, sep="")
        
    # the default value for user input
    user_in = "0"
    # while the input of this menu is not valid we keep trying new input
    while not input_valid:
        user_in = input("=>")
        # verify user input on the menu
        # check if the input is a digit and within range of the options given.
        if re.match("\d+", user_in) and int(user_in) <= range_options:
            input_valid = True
        else:
            print("Foute invoer. Probeer alstublieft opnieuw!")
    # load the function from this link
    options[int(user_in)-1].link()