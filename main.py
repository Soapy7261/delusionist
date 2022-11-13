from data.utility import TextColors as Colors
from data.utility import clear

menu = ""

while not (menu == "A" or menu == "B" or menu == "C" or menu == "D"):
    menu = input(f"""
{Colors.Magenta}THE DELUSIONIST
{Colors.Bright_Green}A game by Fyuki Games

{Colors.Green}A) Play Game
{Colors.Bright_Yellow}B) Settings (W.I.P.)
{Colors.Yellow}C) Credits
{Colors.Red}D) Exit{Colors.Reset}
""").upper()

if menu == "A":
    from src.game.playthrough import gameplay

if menu == "B":
    from src.settings import set

if menu == "C":
    from src.game import credits

if menu == "D":
    exit("Exiting the game for you. Please come again later!")