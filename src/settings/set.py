from data.utility import TextColors as Colors
from data.utility import clear
import json

import os

def settingDisplay():
    settingChoose = ""
    changedSetting = {"flushing": True}
    setValue = ""

    while not (settingChoose == 'A' or settingChoose == 'Cancel'):
        clear()
        with open('src/settings/settings.json') as fp:
            settings = json.loads(fp.read())

        settingChoose = input(f"""
What setting would you like to change?
(Type "{Colors.Yellow}Cancel{Colors.Reset}" to cancel)

A) {Colors.Green if settings['flushing'] == 'True' else Colors.Red}Segmental flushing: {settings['flushing']}{Colors.Reset}""").capitalize()

    if settingChoose == "Cancel":
        clear()
        return # should exit function, doesnt


    while not (setValue == "True" or setValue == "False" or setValue == "Cancel"):
        setValue = input(f"Would you like to set this setting to \"{Colors.Green}True{Colors.Reset}\" or \"{Colors.Red}False{Colors.Reset}\"? Type {Colors.Yellow}\"Cancel{Colors.Reset}\" to cancel.").capitalize()

    if setValue == "Cancel":
        pass

    elif setValue == "True":
        changedSetting = {
            "flushing": setValue
        }
    else:
        changedSetting = {
            "flushing": setValue
        }


    with open('src/settings/settings.json', 'w') as outfile:
        json.dump(changedSetting, outfile)
    settingDisplay()
