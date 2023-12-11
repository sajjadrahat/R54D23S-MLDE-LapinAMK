import functions

maintenance_data = functions.previos_maintenance_data()
functions.latest_maintenance_report(maintenance_data)

name = input("Name: \n")
situation_code = input("Situation code: \n")
description = input("Message: \n")

functions.save_maintenance_report(name, situation_code, description)