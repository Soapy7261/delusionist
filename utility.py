import json


class TextColors:
    Reset = "\u001b[0m"
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    Cyan = "\u001b[36m"
    White = "\u001b[37m"

    Bright_Black = "\u001b[30;1m"
    Bright_Red = "\u001b[31;1m"
    Bright_Green = "\u001b[32;1m"
    Bright_Yellow = "\u001b[33;1m"
    Bright_Blue = "\u001b[34;1m"
    Bright_Magenta = "\u001b[35;1m"
    Bright_Cyan = "\u001b[36;1m"
    Bright_White = "\u001b[37;1m"


with open('scenarios.json') as fp:
    data = json.loads(fp.read())


def decisions(selection: str, currentScene: int) -> str:  # Returns the string relevant to the given selection (A,B,C)
    selection = data['parts']['scenarios'][currentScene]['decisions'][0][f'Decision{selection}'][0]
    return selection


def followDecisions(selection: str, currentScene: int) -> str:
    selection = data['parts']['scenarios'][currentScene]['followup'][0][f'Decision{selection.upper()}'][0]
    return selection


def answerHandling(selection: str, currentScene: int) -> str:
    result = data['parts']['scenarios'][currentScene]['decisions'][0][f'Decision{selection.upper()}'][1]

    if result == "False":
        return data['parts']['scenarios'][currentScene]['Death']
    elif result == "True":
        return "point"
    elif result == "follow":
        mainDecision = ""

        while not (mainDecision == "a" or mainDecision == "b"):
            mainDecision = input(f"""
You must make a choice. {TextColors.Red}Best you be careful,
because the wrong choice could mean the end of you...{TextColors.Yellow}
A >> {followDecisions("A", currentScene)}
B >> {followDecisions("B", currentScene)} 
Answer here: """).lower()

        if data['parts']['scenarios'][currentScene]['followup'][0][f'Decision{mainDecision.upper()}'][1] == "True":
            return "point"
        else:
            return data['parts']['scenarios'][currentScene]['followup'][0]['Death']


answerHandling("A", 1)
