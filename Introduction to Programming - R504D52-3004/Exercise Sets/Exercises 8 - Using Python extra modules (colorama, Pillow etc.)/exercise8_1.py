from colorama import Fore
import datetime

years_list= [int(input(f"{Fore.GREEN}Give the birth year of person {i + 1}: \n" )) for i in range(5)]

print("Let's process all birth years...")

current_year = datetime.datetime.now().year
print()
for year in years_list:
    age = current_year - year
    if 0 <= age <= 125:
        print(f"{Fore.GREEN}{age} years old, age OK!")
    else:
        print(f"{Fore.RED}{age} years old, incorrect age.")

print(f"{Fore.GREEN}All done!")