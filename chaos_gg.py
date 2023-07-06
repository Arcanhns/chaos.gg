import random
import string
import time
from os import system
from colorama import init, Fore, Style
from pyfiglet import Figlet
from termcolor import colored

system("title " + "Chaos.gg")

init()  # Initialize colorama

def generate_code():
    section1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    section2 = "".join(random.choices(string.digits, k=4))
    section3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    code = "-".join([section1, section2, section3])
    return code

# Generate ASCII art for "CHAOS.GG"
f = Figlet(font='slant')
ascii_text = f.renderText('CHAOS.GG')

# Generate rainbow-colored ASCII art
rainbow_ascii_text = ""
colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
for char in ascii_text[:-1]:
    color = random.choice(colors)
    rainbow_ascii_text += colored(char, color)
rainbow_ascii_text += colored(ascii_text[-1], 'white')  # Set the last character color to white

print(rainbow_ascii_text)

prompt_color = Fore.YELLOW
input(f"PRESS '{prompt_color}ENTER{Style.RESET_ALL}' TO GENERATE")

codes = []
while len(codes) < 100:
    code = generate_code()
    full_code = "chaos.gg/gift/" + code
    codes.append(full_code)
    print(f"{Fore.YELLOW}[+]{Fore.RESET} {full_code}")
    time.sleep(0.1)  # Introduce a 0.5-second (half a second) delay between code generation

input()