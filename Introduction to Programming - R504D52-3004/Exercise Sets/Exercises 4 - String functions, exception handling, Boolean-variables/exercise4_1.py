from datetime import date

date_today= date.today().strftime("%d.%m.%Y")
client_name= "Sajjad Mahmud Rahat"
year_of_birth = 2002
balance= 100
concat_text= f"{client_name} ({year_of_birth}), balance: {year_of_birth} €, updated on {date_today}"
print(concat_text)

