from datetime import datetime
import json
import random
import csv

# exercise10_1
def read_file_contents(filename):
    with open(filename, "r") as file_handle:
            content_str = file_handle.read()
            content_list = content_str.split("\n")
            return content_list


# exercise10_2
def read_guestbook():
    with open('guestbook.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
                print(line.strip())

def write_guestbook():
    message = input("Write a new message: \n")
    # Using 'a' to append message in txt file.
    with open('guestbook.txt', 'a') as file:
        file.write(message + '\n')

# exercise10_2_extra
def read_guestbook_json():
    with open('guestbook.json', 'r') as json_file:
        messages = json.load(json_file)
        for data in messages:
            print(f"{data['time']} : {data['message']}")

def write_guestbook_json():
    message = input("Write a new message: \n")

    # Read existing messages
    with open('guestbook.json', 'r') as json_file:
        messages = json.load(json_file)

    # Append new message
    new_message = {
        'message': message,
        'time': str(datetime.now())
    }
    messages.append(new_message)

    # Write the updated messages back to the file
    with open('guestbook.json', 'w') as json_file:
        json.dump(messages, json_file, indent=2)

# exercise10_3.py

def random_proverb_generator():
    print("Today's proverb:")
    with open('wisewords.txt', 'r') as file:
        proverb_contents= file.readlines()
        max_lines_index = len(proverb_contents)-1
        random_num = random.randint(0,max_lines_index)
        print(proverb_contents[random_num])

# exercise10_4.py

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

# exercise10_5.py

def previos_maintenance_data():
    try:
        with open('maintenance.json', 'r') as json_file:
            maintenance_data = json.load(json_file)
        return maintenance_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def latest_maintenance_report(maintenance_data):
    if maintenance_data:
        latest_report = maintenance_data[-1]
        print("\nLatest maintenance report...")
        print(f"Date: {latest_report['date']}")
        print(f"By: {latest_report['name']}")
        print(f"Situation code: {latest_report['situation_code']}")
        print(f"Message: {latest_report['description']}")

def save_maintenance_report(name, situation_code, description):
    date_str = datetime.now().strftime('%d.%m.%Y')
    new_report = {
        'date': date_str,
        'name': name,
        'situation_code': situation_code,
        'description': description
    }

    maintenance_data = previos_maintenance_data()
    maintenance_data.append(new_report)

    with open('maintenance.json', 'w') as json_file:
        json.dump(maintenance_data, json_file, indent=2)


# exercise10_6.py

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]
    return data

def print_csv(data):
    for row in data:
        print(', '.join(row))

def increase_salary(data):
    # Row 1 is header, so loop is going to be run after first row
    for row in data[1:]:
            # Salary in last column
            # Getting the salary and converting to int
            current_salary = int(row[4])
            new_salary = current_salary + 100
            row[4] = str(new_salary)

def save_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)


# exercise10_7.py
