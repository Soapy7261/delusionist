import aiohttp
import asyncio
from data.utility import TextColors as Colors
from data.utility import clear

# Get user's name and welcome them

print(f"""
------------------------------------------------------------------------------------------------------------
Welcome! To {Colors.Magenta}The Delusionist{Colors.Reset}. If you are ready to start the game, just say your name.
To get a random name, just type {Colors.Green}random{Colors.Reset}. To stop, type {Colors.Red}stop{Colors.Reset}.

{Colors.Red}This game includes detailed explanations of occuring deaths.
Please exit the game if you do not believe to be up for this.
Death can be common in this game, so please be wary of this.{Colors.Reset}

{Colors.Magenta}The Delusionist{Colors.Reset} is a game developed, and owned by Fyuki Games.
https://github.com/FyukiGames - a company by MiataBoy (https://github.com/MiataBoy)
------------------------------------------------------------------------------------------------------------
""")

while not (username := input(f"{Colors.Green}Enter your name here: {Colors.Reset}").capitalize()).isalpha():
    print(f"{Colors.Red}Please only use letters.{Colors.Reset}")

# Fail if name is a digit because usually human names do not consist of digits
if username == "Stop":
    print(f"{Colors.Yellow}User requested to exit game, exiting...{Colors.Reset}")
    exit()


# Set the name of the user to what they set, or connect and get name from randomuser.me API if they choose for a random name

clear()

async def main():
    if username == "Random":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomuser.me/api/") as response:
                    firstname = await response.json()
                    global name
                    name = firstname['results'][0]['name']['first']
        except BaseException as error:
            print("API not found - Assigning fallback name Miat")
            name = "Miat"
    else:
        name = username

# Introduce the game
asyncio.run(main())

input(f"""
{Colors.Bright_Green}You are playing {name}. A man suffering from delusions, hallucinations and traumas originating from his childhood.
He was helpless, unable to provide for himself and unable to be provided to, his only choice being to seek shelter in an abandoned mansion.{Colors.Reset}
{Colors.Red}Unfortunately, little would prepare him for the horrors he would encounter...{Colors.Reset}

Press ENTER to continue.
""")

clear()