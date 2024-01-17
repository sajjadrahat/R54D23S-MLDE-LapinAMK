from datetime import datetime
import json

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

user_input = input("Would you like to read or write into the guestbook? (r/w)\n")

if user_input=="r":
    read_guestbook_json()
elif user_input=="w":
    write_guestbook_json()