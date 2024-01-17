import math
import random
import urllib.request
import json
import operator

# exercise9_1
def show_personal_info():
    name = "John Williams"
    address = "Rovaniemi"
    profession = "Software engineer"

    print(name)
    print(address)
    print(profession)

#  exercise9_2.py
def count_seconds(hours, minutes, seconds):
    total_seconds = hours*60*60 + minutes*60 + seconds
    return f"{total_seconds} seconds in total."

#  exercise9_3.py
def magazine_serial_check(serial):
    flag = False
    if serial[4]=="-":
        serial_without_dash = serial.replace("-", "")
        if len(serial_without_dash) == 8:
            if serial_without_dash.isdigit():
                flag= True
    return flag

#  exercise9_4.py
def show_numbered_list(title, people):
    # Extra blank so that it looks good as data
    print()
    print(title)
    count=1
    for name in people:
        print(f"{count}. {name}")
        count+=1

#  exercise9_5.py

def box_volume(width, height, depth):
    # formula = width * height * depth
    result = width*height*depth
    return round(result,2)

def ball_volume(radius):
    # formula = (4 * π * radius^3) / 3
    result= (4* math.pi * math.pow(radius, 3)) / 3
    return round(result, 2)

def pipe_volume(radius, length):
    # formula = π * radius^2 * length
    result= math.pi * math.pow(radius, 2) * length
    return round(result, 2)

# exercise9_6.py

def lotteryNumberGenerator():
    lottery_series=[]
    while len(lottery_series)!=7:
        rand_num= random.randint(1, 40)
        if rand_num not in lottery_series:
            lottery_series.append(rand_num)
    # Printing the series without bracket and instead of comma i am using space
    formatted_lottery_series = " ".join(map(str, lottery_series))
    print(f"Generated lotto number: {formatted_lottery_series}")

# exercise9_8.py

def convert_money(user_input_amount, currency):
    url = "https://open.er-api.com/v6/latest/EUR"

    req = urllib.request.Request(url)
    raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
    exchange_rate_data = json.loads(raw_data)
    rate = exchange_rate_data.get("rates", {}).get(currency)
    converted_amount= round(user_input_amount*rate, 2)
    print(f"{user_input_amount} EUR == {converted_amount} {currency}")


# exercise9_11.py
def city_landmark_sort(data):
    # Calling operator module it is faster and convinient then lambda.
    data = sorted(data, key=operator.itemgetter('city', 'landmark'))
    return data