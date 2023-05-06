from pyfiglet import Figlet
import sys
import random


def main():
    get_font()

def get_font():
    figlet = Figlet()
    get_font = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(get_font))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font = sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print("Output: \n", figlet.renderText(text))

main()
