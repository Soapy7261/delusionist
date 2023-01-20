import asyncio
import aiohttp
import json
import utility
from utility import TextColors as Colors

introductionary = True
playScene = 0
points = 0

while introductionary:
    print(f"""
------------------------------------------------------------------------------------------------------------
Welcome! To {Colors.Magenta}The Delusionist{Colors.Reset}. If you are ready to start the game, just say your name.
To get a random name, just type {Colors.Green}random{Colors.Reset}. To stop, type {Colors.Red}stop{Colors.Reset}.
{Colors.Red}This game includes detailed explanations of occuring deaths.
Please exit the game if you do not believe to be up for this.
Death can be common in this game, so please be wary of this.{Colors.Reset}
------------------------------------------------------------------------------------------------------------
""")

    while not (username := input(f"{Colors.Green}Enter your name here: {Colors.Reset}").capitalize()).isalpha():
        print(f"{Colors.Red}Please only use letters (without spaces).{Colors.Reset}")

    # Fail if name is a digit because usually human names do not consist of digits
    if username == "Stop":
        print(f"{Colors.Yellow}User requested to exit game, exiting...{Colors.Reset}")
        exit()

    async def main() -> str:
        if username == "Random":
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://randomuser.me/api/") as response:
                        firstname = await response.json()
                        return firstname['results'][0]['name']['first']
            except BaseException as error:
                print("API did not return as expected - assigning fallback name")
                return "Miataboy"
        else:
            return username

    username = asyncio.run(main())

    introduction = input(f"""
{Colors.Bright_Green}You are playing {username}. A man suffering from delusions, hallucinations and traumas originating from his childhood.
He was helpless, unable to provide for himself and unable to be provided to, his only choice being to seek shelter in an abandoned mansion.{Colors.Reset}
{Colors.Red}Unfortunately, little would prepare him for the horrors he would encounter...{Colors.Reset}
{Colors.Bright_Blue}Submit any character to begin.{Colors.Reset}
""")

    with open('data/scenes.json') as fp:
        data = json.loads(fp.read())

    print(len(data[0]['scenarios']))

    while playScene < len(data[0]['scenarios']):
        # Variables for the game to work
        mainDecision = ""

        print(f"{Colors.Bright_Blue}Congratulations! Part {playScene+1} has been unlocked.{Colors.Reset}")

        print(data[2]['stories'][f'Scenario{playScene}'])

        while not (mainDecision == "A" or mainDecision == "B" or mainDecision == "C" or mainDecision == "Stop"):
            mainDecision = input(f"""
You must make a choice. {Colors.Red}Best you be careful,
because the wrong choice could mean the end of you...{Colors.Yellow}

{Colors.Reset}{data[0]['scenarios'][playScene]['question']}

A >> {utility.decisions("A", playScene)}
B >> {utility.decisions("B", playScene)} 
C >> {utility.decisions("C", playScene)}
{Colors.Bright_Blue}Want to stop? Simply type "stop" to stop.{Colors.Reset}
Answer here: """).upper()

        if mainDecision == "Stop":
            playScene = len(data['parts']['scenarios'])
        else:
            action = utility.answerHandling(mainDecision, playScene)
            if action == "point":
                points += 1
                playScene += 1
            elif action == "nopoint":
                playScene += 1
            else:
                print(action)
                playScene = len(data[0]['scenarios'])

    # THE WHILE LOOP ENDS HERE, PAST THIS POINT ONLY HANDLES PLAYING AGAIN

    playAgain = ""
    while not (playAgain == "y" or playAgain == "n"):
        playAgain = input("Would you like to play again? Y/N")

    if playAgain == "n":
        introductionary = False
        print(f"You have finished the game with a total of {points} points.")

    elif playAgain == "y":
        print(f"Restarting game... You ended this playthrough on {points} points.")
        points = 0
        playAgain = ""
        playScene = 0