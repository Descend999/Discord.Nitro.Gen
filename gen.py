import random, string
from colorama import Fore as Color
from colorama import Fore, Back, Style

print(f"""

{Color.MAGENTA} ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████
{Color.MAGENTA} ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒
{Color.MAGENTA}▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒
{Color.MAGENTA}▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░
{Color.MAGENTA}▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░
{Color.MAGENTA}░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
{Color.MAGENTA}░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ 
{Color.MAGENTA}   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒  
{Color.MAGENTA}         ░  ░              ░         ░ ░                            
""")

amount = int(input(f'{Color.GREEN}Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'{Color.RED}[{Color.BLUE}GENERATED{Color.RED}]{Color.RESET} {code}')
    value += 1
