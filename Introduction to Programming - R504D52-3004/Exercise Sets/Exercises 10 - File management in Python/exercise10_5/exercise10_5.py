import json
from datetime import datetime

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


maintenance_data = previos_maintenance_data()
latest_maintenance_report(maintenance_data)

name = input("Name: \n")
situation_code = input("Situation code: \n")
description = input("Message: \n")

save_maintenance_report(name, situation_code, description)