import os
import platform

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def show():
    clear_screen()
    print(RED + BOLD + r"""
   _       __               __  ____                 
  | |     / /___  _________/ / / __ \____  __________
  | | /| / / __ \/ ___/ __  / / /_/ / __ `/ ___/ ___/
  | |/ |/ / /_/ / /  / /_/ / / ____/ /_/ (__  )__  ) 
  |__/|__/\____/_/   \__,_/ /_/    \__,_/____/____/  
""" + RESET)
    
    print(CYAN + "      >>> WordPass Generator <<<" + RESET)
    print(GREEN + "-" * 70 + RESET)
    print("\n")