from data.utility import TextColors as Colors
from data.utility import clear
import json

import json
import os

def where_json(file_name):
    return os.path.exists(file_name)


if where_json(os.path.abspath("src/settings/settings.json")):
    print("Settings file exists")
    print(os.path.abspath("src/settings/settings.json"))
    pass

else:
    print("{}WARNING: Settings file not found, creating one...".format(Colors.Yellow))
    data = {
 "flushing": "True"
    }

    with open('src/settings/settings.json', 'w') as outfile:
        json.dump(data, outfile)

    print("{}Settings file created successfully.".format(Colors.Green))

menu = ""
while True:
    while not (menu == "A" or menu == "B" or menu == "C" or menu == "D"):
        menu = input(f"""
    {Colors.Magenta}THE DELUSIONIST
    {Colors.Bright_Green}A game by Fyuki Games
    
    {Colors.Green}A) Play Game
    {Colors.Bright_Yellow}B) Settings (Coming later)
    {Colors.Yellow}C) Credits
    {Colors.Red}D) Exit{Colors.Reset}
    """).upper()

    if menu == "A":
        from src.game.playthrough import gameplay

    if menu == "B":
        from src.settings.set import settingDisplay
        settingDisplay()

    if menu == "C":
        from src.game import credits

    if menu == "D":
        exit("Exiting the game for you. Please come again later!")