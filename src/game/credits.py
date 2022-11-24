import os

from data.utility import TextColors as Colors
from data.utility import clear

def credit():
    input(f"""
    {Colors.Magenta}The Delusionist{Colors.Reset} is a game made by {Colors.Bright_Blue}Fyuki Games{Colors.Reset}
    Fyuki Games is a netherlands-based text-based game and project development studio;
    Owned by {Colors.Bright_Blue}MiataBoy{Colors.Reset}, and development being upheld by the community and its developers..
    
    You can find all contributors here:
    {Colors.Bright_Blue}https://github.com/FyukiGames/delusionist/graphs/contributors
    
    {Colors.Reset}Organization links:
    {Colors.Bright_Blue}https://github.com/FyukiGames
    https://discord.gg/wf89Guxdjb
    
    {Colors.Reset}MiataBoy socials:
    {Colors.Bright_Blue}https://github.com/MiataBoy
    https://twitter.com/MiataBoyMX
    
    Press [ENTER] to return to main screen
    """)

    clear()
    return
# Make into function
