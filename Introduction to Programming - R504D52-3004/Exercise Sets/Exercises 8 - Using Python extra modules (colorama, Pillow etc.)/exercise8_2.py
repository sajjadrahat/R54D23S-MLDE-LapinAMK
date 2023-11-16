from colorama import Fore, Back, Style
import random

random_num= random.randint(1,20)
while True:
    num_guess= int(input(f"{Fore.GREEN}Guess the number (1-20) \n"))
    if num_guess==random_num:
        print(f"{Back.GREEN}CONGRATULATIONS!!{Style.RESET_ALL}\n")
        break
    elif num_guess>random_num:
        print(f"{Back.RED}Too high.{Style.RESET_ALL}\n")
    elif num_guess<random_num:
        print(f"{Back.BLUE}Too low.{Style.RESET_ALL}\n")    