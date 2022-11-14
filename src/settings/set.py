from data.utility import TextColors as Colors
from data.utility import clear

import os

enter = input(f"""
{Colors.Red}We are sorry for the inconvenience, but we ran into some issues with the settings menu :(
{Colors.Reset}We are working hard to resolve this (Check back in our discord sometimes!)
You can find our discord here: https://discord.gg/wf89Guxdjb

{Colors.Green}For now, we can give you steps to changing the settings through our settings file.{Colors.Reset}

1) Go to {Colors.Green}file://{os.path.dirname(os.path.abspath(__file__))}/settings.json{Colors.Reset}
2) Change the desired setting to either "True" or "False". Anything else may break it- or assign it to a specific value.
3) Save the file
4) Exit the game
5) Start the game back up and enjoy!

{Colors.Yellow}Default Configuration:{Colors.Reset}
{'{'}
  "flushing": "{Colors.Green}True{Colors.Reset}"
{'}'}

{Colors.Yellow}What settings do:{Colors.Reset}
Flushing: Flushing enables clearing of the console before each new segment in the game
""")

clear()
exit(os.system('python main.py'))
#settingChoose = ""
#settingSetting = ""
#exiting = False

#with open('src/settings/settings.json') as fp:
#    settings = json.loads(fp.read())

#while exiting == False:
#    while not (settingChoose == "A" or settingChoose == "Exit"):
#        settingChoose = input(f"""
#Please choose one of the following settings to edit or type \"exit\" to exit:
#({Colors.Yellow}Settings can only be changed to {Colors.Green}\"True\" {Colors.Yellow}or {Colors.Red}\"False\"{Colors.Reset})

#{Colors.Blue}A) Console Flushing [Clears console before each new segment]:{Colors.Green if settings["flushing"] == "True" else Colors.Red} {settings["flushing"]}{Colors.Reset}
#    """).upper()

#    if settingChoose == "A":
#        while not (settingSetting == "True" or settingSetting == "False" or settingSetting == "Exit"):
#            settingSetting = input(f"Would you like to set this to {Colors.Green}\"True\" {Colors.Reset}or {Colors.Red}\"False\"{Colors.Reset}?").upper()

#        if settingSetting == "True":
#            settings["flushing"] = True
#            break
#        if settingSetting == "False":
#            settings["flushing"] = False
#            break
#        if settingSetting == "Exit":
#            break

#    if settingChoose == "Exit":
#        break



