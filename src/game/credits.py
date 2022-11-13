import os

from data.utility import TextColors as Colors

input(f"""
{Colors.Magenta}The Delusionist{Colors.Reset} is a game made by {Colors.Bright_Blue}Fyuki Games{Colors.Reset}
Fyuki Games is a netherlands-based one-man text-based game and project development studio;
Owned by {Colors.Bright_Blue}MiataBoy{Colors.Reset}, and development being upheld entirely by him and the community.

You can find all contributors here:
{Colors.Bright_Blue}https://github.com/FyukiGames/delusionist/graphs/contributors

{Colors.Reset}Organization links:
{Colors.Bright_Blue}https://github.com/FyukiGames
<Discord incoming soon>

{Colors.Reset}MiataBoy socials:
{Colors.Bright_Blue}https://github.com/MiataBoy
https://twitter.com/MiataBoyMX

Press [ENTER] to return to main screen
""")

exit(os.system('python main.py'))