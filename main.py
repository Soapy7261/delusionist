import random

import aiohttp
import asyncio
import json
import datetime
from data.utility import TextColors as Colors

# Get user's name and welcome them

name = str()

print(f"""
------------------------------------------------------------------------------------------------------------
Welcome! To {Colors.Magenta}The Delusionist{Colors.Reset}. If you are ready to start the game, just say your name.
To get a random name, just type {Colors.Green}random{Colors.Reset}. To stop, type {Colors.Red}stop{Colors.Reset}.

{Colors.Red}This game includes detailed explanations of occuring deaths.
Please exit the game if you do not believe to be up for this.
Death can be common in this game, so please be wary of this.{Colors.Reset}

{Colors.Magenta}The Delusionist{Colors.Reset} is a game developed, and owned by FyukiGames.
------------------------------------------------------------------------------------------------------------
""")

while not (username := input(f"{Colors.Green}Enter your name here: {Colors.Reset}").capitalize()).isalpha():
    print(f"{Colors.Red}Please only use letters.{Colors.Reset}")

# Fail if name is a digit because usually human names do not consist of digits
if username == "Stop":
    print(f"{Colors.Yellow}User requested to exit game, exiting...{Colors.Reset}")
    exit()


# Set the name of the user to what they set, or connect and get name from randomuser.me API if they choose for a random name

async def main():
    if username == "Random":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomuser.me/api/") as response:
                    firstname = await response.json()
                    print("Welcome {}. Enjoy the game.".format(firstname['results'][0]['name']['first']))
                    global name
                    name = firstname['results'][0]['name']['first']
        except BaseException as error:
            print("API not found")
            name = "Yata"
    else:
        print("Welcome {}. Enjoy the game.".format(username))
        name = username


# Introduce the game
asyncio.run(main())
print(f"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
You are playing {name}. A man grown up with traumas and issues, that have caused a life long trauma and a life filled with delusions, and seeing things that aren't there.
No one could help {name}, and maintaining a job or a home, was not viable for him. He took refugee in an abandoned mansion,
but little could prepare him for the horrors that the mansion would bring him, together with his issues.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")

gameVar = 0
count = 0
scenario = 0

while gameVar == 0:
    with open('data/scene.json') as fp:
        data = json.loads(fp.read())

        try:
            data['parts']['scenarios'][scenario]['scenario']
        except:
            if IndexError:
                print(
                    'You have managed to escape the mansion, and been granted the help you needed. From here on, your life could only improve... Congratulations')
                exit()

        print("You have unlocked Scenario {}. Congratulations on surviving.".format(scenario + 1))

        print("\n", data['parts']['story'][0]['Scenario{}'.format(scenario)])

        answer = input(f"""
-------------------------------------------------------------------------------------
A choice presents itself... What will {name} choose?

{data['parts']['scenarios'][scenario]['scenario']}
[A] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionA'][0]}
[B] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionB'][0]}
[C] {data['parts']['scenarios'][scenario]['decisions'][0]['DecisionC'][0]}

Beware:  Sometimes your choice may be lethal to {name}, and submitting something else will always be lethal.
-------------------------------------------------------------------------------------
""").lower()


        def answered(result):
            if result == "False":
                print(data['parts']['scenarios'][scenario]['Death'].replace("NAME", name))
                exit()
            if result == "True":
                pass

            if result == "follow" and data['parts']['scenarios'][scenario]['followup'] != "null":
                fanswer = input(f"""
{data['parts']['scenarios'][scenario]['followup'][0]['Story']}

-------------------------------------------------------------------------------------
A follow-up choice presents itself... What will {name} choose?

{data['parts']['scenarios'][scenario]['followup'][0]['Question']}
[A] {data['parts']['scenarios'][scenario]['followup'][0]['DecisionA'][0]}            
[B] {data['parts']['scenarios'][scenario]['followup'][0]['DecisionB'][0]}

Beware:  Sometimes your choice may be lethal to {name}, and submitting something else will always be lethal.
-------------------------------------------------------------------------------------
            """).lower()
                if fanswer == "a":
                    fresult = data['parts']['scenarios'][scenario]['followup'][0]['DecisionA'][1]
                    if fresult == "False":
                        print(data['parts']['scenarios'][scenario]['followup'][0]['Death'].replace("NAME", name))
                        exit()
                    else:
                        pass
                if fanswer == "b":
                    fresult = data['parts']['scenarios'][scenario]['followup'][0]['DecisionB'][1]
                    if fresult == "False":
                        print(data['parts']['scenarios'][scenario]['followup'][0]['Death'].replace("NAME", name))
                        exit()
                    else:
                        pass
            else:
                pass


        if answer == "stop":
            print("User has requested to abort the game, Exiting...")
            exit()
        elif answer == "a":
            result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionA'][1]
            answered(result)
        elif answer == "b":
            result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionB'][1]
            answered(result)
        elif answer == "c":
            result = data['parts']['scenarios'][scenario]['decisions'][0]['DecisionC'][1]
            answered(result)
        else:
            today = datetime.datetime.now()
            print(
                f"You have decided to do nothing. This, clearly was not a good idea as you have starved of hunger.\nRest in Peace {name}, 1993-{today.strftime('%Y')}")
            exit()

        scenario += 1