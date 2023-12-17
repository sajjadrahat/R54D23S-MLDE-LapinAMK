import json

def country_capital_list():
    print("All countries and capitals:")
    with open('countries.json', 'r') as json_file:
        country_capital = json.load(json_file)
    for data in country_capital:
        print(f"{data['country']} : {data['capital']}")

    user_input = input("Filter a country/capital with a starting letter: \n")
    for data in country_capital:
        country= data['country']
        capital = data['capital']
        # Using 'startswith' and 'or' condition to filter data
        # I think there is some mistake on the instructions
        # Example output shows only countries that starts with the letter 'S'
        # But in question it is given country/capital to filter out.
        if str(country).startswith(user_input) or str(capital).startswith(user_input):
            print(f"{country} : {capital}")

country_capital_list()