import time
import os
from pycenter import center
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

calculator = f'''{Fore.GREEN}


{Fore.RED}       ┍ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ┑
{Fore.RED}       |{Fore.BLUE}   ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗   {Fore.RED} |
{Fore.RED}       |{Fore.BLUE}  ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗  {Fore.RED} |
{Fore.RED}       |{Fore.BLUE}  ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝  {Fore.RED} |
{Fore.RED}       |{Fore.BLUE}  ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗  {Fore.RED} |
{Fore.RED}       |{Fore.BLUE}  ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║  {Fore.RED} |
{Fore.RED}       |{Fore.BLUE}   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝  {Fore.RED} |
{Fore.RED}       ┕ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ┙
'''
discord = f'''{Fore.RED}

┍ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ┑
|  {Fore.BLUE}GitHUB : https://github.com/Glaxifiak    {Fore.RED}|
┕ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ┙
┍ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ┑
|  {Fore.BLUE}discord : https://discord.gg/PZaC29DqgA  {Fore.RED}|
┕ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ┙
'''

result = f'''{Fore.RED}
{Fore.RED}      ┍ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┑
{Fore.RED}      |{Fore.GREEN}  ██████╗ ███████╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ████████╗ {Fore.RED} |
{Fore.RED}      |{Fore.GREEN}  ██╔══██╗██╔════╝██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗╚══██╔══╝ {Fore.RED} |
{Fore.RED}      |{Fore.GREEN}  ██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ███████║   ██║    {Fore.RED} |
{Fore.RED}      |{Fore.GREEN}  ██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ██╔══██║   ██║    {Fore.RED} |
{Fore.RED}      |{Fore.GREEN}  ██║  ██║███████╗███████║╚██████╔╝███████╗██║   ██║  ██║   ██║    {Fore.RED} |
{Fore.RED}      |{Fore.GREEN}  ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝   ╚═╝    {Fore.RED} | 
{Fore.RED}      ┕ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┙                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
'''


clear = lambda: os.system('cls')
clear()
print(center(calculator))
print(center(discord))


nombre = int(input("Entre le premier nombre : \n"))
combien_mult = int(input("Tu veux que ça multiplis durant combien de tour ? : \n"))
par_combien = int(input("Tu veux que " + str(nombre) + " sois multiplier par combien à chaque fois : \n"))
save = input("Voulez vous save le resultat ? (y/n) \n")    
if save == 'y':
    name = input("Entrer le nom que vous voulez atribuer a votre fichier (Oublier pas le .txt) : \n")
unité_one = input("Voulez mettre une unité de mesure ? (y/n) : \n") 
if unité_one == 'y':
    unité = input("Laquelle : \n")


def clearrrr():
    clear = lambda: os.system('cls')
    clear()
    time.sleep(1)

if __name__ == '__main__':
    clearrrr()

print(center(result))

if unité_one == 'y' :
    for k in range(combien_mult):
        nombre = nombre * par_combien
        time.sleep(0.2)
        print(center(f"{Fore.GREEN} "+ str(nombre)+" "+ unité ))

if unité_one == 'n' :
    for k in range(combien_mult):
        nombre = nombre * par_combien
        time.sleep(0.2)
        print(center(f"{Fore.GREEN} "+ str(nombre)))


if unité_one == 'n':
    print(center(f"{Fore.GREEN}Voila le resultat : " + str(nombre) + " | Votre premier nombre a été multiplier pendant " + str(combien_mult) + " tour par " + str(par_combien) +" à chaque fois ! "  ))

if unité_one == 'y':
    print(center(f"{Fore.GREEN}Voila le resultat : " + str(nombre) + " " + unité + " | Votre premier nombre a été multiplier pendant " + str(combien_mult) + " tour par " + str(par_combien) +" à chaque fois ! "  ))




if save == 'y' and unité_one == 'n' :
    Resultat_Caclcul = open(name, "x")
    Resultat_Caclcul.write("Le resultat de votre calcule est : "+ str(nombre))
    Resultat_Caclcul.close()

if save == 'y' and unité_one == 'y' :
    Resultat_Caclcul = open(name, "x")
    Resultat_Caclcul.write("Le resultat de votre calcule est : "+ str(nombre)+" "+ unité)
    Resultat_Caclcul.close()

