#import json
#import datetime
# from data.utility import TextColors as Colors
# from data.utility import clear
#
# gameVar = 0
# count = 0
# scenario = 0
#
# with open('data/userdata.json') as up:
#     userdata = json.loads(up.read())
#
# name = userdata["user"]["name"]
#
# while gameVar == 0:
#     with open('data/scene.json') as fp:
#         data = json.loads(fp.read())
#
#         try:
#             data['parts']['scenarios'][scenario]['scenario']
#         except:
#             if IndexError:
#                 print('You have managed to escape the mansion, and been granted the help you needed. From here on, your life could only improve... Congratulations')
#
#                 exit()
#
#         input(f"Scenario {scenario + 1}:\n{data['parts']['story'][0][f'Scenario{scenario}']}\n\n{Colors.Green}Press [ENTER] to continue{Colors.Reset}")
#
#         clear()
#
#         answer = input(f"""
# {Colors.Red}A choice presents itself... What will {name} choose?
#
# {Colors.Yellow}{data['parts']['scenarios'][scenario]['scenario']}{Colors.Reset}
# [A] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionA'][0]}
# [B] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionB'][0]}
# [C] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionC'][0]}
#
# {Colors.Red}Beware: Sometimes your choice may be lethal to {name}, and submitting something else will always be lethal.{Colors.Reset}
# """).lower()
#
#
#         def answered(result):
#             if result == "False":
#                 print(data['parts']['scenarios'][scenario]['Death'].replace("NAME", name))
#                 exit()
#             if result == "True":
#                 pass
#
#             if result == "follow" and data['parts']['scenarios'][scenario]['followup'] != "null":
#                 fanswer = input(f"""
# {data['parts']['scenarios'][scenario]['followup'][0]['Story']}
#
# -------------------------------------------------------------------------------------
# A follow-up choice presents itself... What will {name} choose?
#
# {data['parts']['scenarios'][scenario]['followup'][0]['Question']}
# [A] {data['parts']['scenarios'][scenario]['followup'][0]['DecisionA'][0]}
# [B] {data['parts']['scenarios'][scenario]['followup'][0]['DecisionB'][0]}
#
# Beware:  Sometimes your choice may be lethal to {name}, and submitting something else will always be lethal.
# -------------------------------------------------------------------------------------
#             """).lower()
#                 if fanswer == "a":
#                     fresult = data['parts']['scenarios'][scenario]['followup'][0]['DecisionA'][1]
#                     if fresult == "False":
#                         print(data['parts']['scenarios'][scenario]['followup'][0]['Death'].replace("NAME", name))
#                         exit()
#                     else:
#                         pass
#                 if fanswer == "b":
#                     fresult = data['parts']['scenarios'][scenario]['followup'][0]['DecisionB'][1]
#                     if fresult == "False":
#                         print(data['parts']['scenarios'][scenario]['followup'][0]['Death'].replace("NAME", name))
#                         exit()
#                     else:
#                         pass
#             else:
#                 pass
#
#
#         if answer == "stop":
#             print("User has requested to abort the game, Exiting...")
#             exit()
#         elif answer == "a":
#             result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionA'][1]
#             answered(result)
#         elif answer == "b":
#             result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionB'][1]
#             answered(result)
#         elif answer == "c":
#             result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionC'][1]
#             answered(result)
#         else:
#             today = datetime.datetime.now()
#             print(f"You have decided to do nothing. This, clearly was not a good idea as you have starved of hunger.\nRest in Peace {name}, 1993-{today.strftime('%Y')}")
#             exit()
#
#         scenario += 1
# We can do this better:

import json
from data.utility import hibernate, clear
from data.utility import TextColors as Colors

# Variables essential to game runtime
gamePlay = True
scenario = 0
mainDecision = ""
FollowDecision = ""

# JSON connection
with open('data/userdata.json') as up:
    userdata = json.loads(up.read())

name = userdata['user']['name']

while gamePlay:
    with open('data/scenes.json') as fp:
         data = json.loads(fp.read())

    # Answer filter function
    def funcAnswer(userAnswer: str) -> str:
        userAnswer = "This is in progress."
        return userAnswer

    def decisions(selection: str) -> str: # Returns the string relevant to the given selection (A,B,C)
        selection = data['parts']['scenarios'][scenario]['decisions'][0][f'Decision{selection}'][0]
        return selection

    def decisionsRes(selection: str) -> str: # Returns the result string relevant to the given selection (A,B,C)
        selection = data['parts']['scenarios'][scenario]['decisions'][0][f'Decision{selection}'][1]
        return selection

    def followDecisions(selection: str) -> str: # Returns the string relevant to the given selection (A,B)
        selection = data['parts']['scenarios'][scenario]['followup'][0][f'Decision{selection}'][0]
        return selection

    def followDecisionsRes(selection: str) -> str: # Returns the result string relevant to the given selection (A,B)
        selection = data['parts']['scenarios'][scenario]['followup'][0][f'Decision{selection}'][1]
        return selection


    print(f"Scenario {scenario + 1}:\n{data['parts']['story'][0][f'Scenario{scenario}']}\n\n{Colors.Green}Continuing in 30 seconds...{Colors.Reset}")

    hibernate(5)

    while not (mainDecision == "a" or mainDecision == "b" or mainDecision == "c" or mainDecision == "stop"):
        mainDecision = input(f"""
You must make a choice. {Colors.Red}Best you be careful,
because the wrong choice could mean the end of you...{Colors.Yellow}

A >> {decisions("A")}
B >> {decisions("B")} 
C >> {decisions("C")}

{Colors.Reset}Want to stop? Simply type "stop" to stop.
Answer here: """).lower()

    if mainDecision == "stop":
        gamePlay = False

