import functions

user_input_amount = int(input("Give money in original currency (EUR): \n"))
user_currency_convert = int(input("Which currency you want to convert? \nType: 1 --> Convert to USD ($)\nType: 2 --> Convert to Pound (£)\n"))
if user_currency_convert==1:
    currency= "USD"
elif user_currency_convert==2:
    currency= "GBP"
functions.convert_money(user_input_amount, currency)