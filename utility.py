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


with open('data/scenes.json') as fp:
    data = json.loads(fp.read())

# x[0].scenarios[1]

def decisions(selection: str, currentScene: int) -> str:  # Returns the string relevant to the given selection (A,B,C)
    selection = data[0]['scenarios'][currentScene]['answers']['answerKeys'][f'Decision{selection}']
    return selection


def followDecisions(selection: str, currentScene: int) -> str:
    selection = data[1]['follows'][currentScene]['answers']['answerKeys'][f'Decision{selection}']
    return selection


def answerHandling(selection: str, currentScene: int) -> str:
    print(data[0]['scenarios'][0]['answers']['answerValues']['DecisionA'])
    result = data[0]['scenarios'][currentScene]['answers']['answerValues'][f'Decision{selection}']

    if result == "False":
        return data[0]['scenarios'][currentScene]['Death']
    elif result == "True":
        return "point"
    elif result == "Trail":
        mainDecision = ""

        while not (mainDecision == "a" or mainDecision == "b"):
            mainDecision = input(f"""
You must make a choice. {TextColors.Red}Best you be careful,
because the wrong choice could mean the end of you...{TextColors.Yellow}
A >> {followDecisions("A", currentScene)}
B >> {followDecisions("B", currentScene)} 
Answer here: """).lower()

        if data[1]['follows'][currentScene]['answers']['answerValues'][f'Decision{selection}']  == "True":
            return "nopoint"
        else:
            return data[1]['follows'][currentScene]['death']