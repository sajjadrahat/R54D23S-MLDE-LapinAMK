import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)
print(weather)
strongest_wind = {"city": "", "wind_speed": 0}
weakest_wind = {"city": "", "wind_speed": 0}

wind_speeds_by_area = {"lapland": [], "middle": [], "south": []}

for item in weather:
    city = item["location"]
    wind_speed = item["wind"]
    area = item["area"]
    if wind_speed > strongest_wind["wind_speed"]:
        strongest_wind["city"] = city
        strongest_wind["wind_speed"] = wind_speed

    if wind_speed < weakest_wind["wind_speed"] or weakest_wind["wind_speed"] == 0:
        weakest_wind["city"] = city
        weakest_wind["wind_speed"] = wind_speed

    wind_speeds_by_area[area].append(wind_speed)

print(f"Strongest wind today at location: {strongest_wind['city']}, {strongest_wind['wind_speed']} m/s")
print(f"Weakest wind today at location: {weakest_wind['city']}, {weakest_wind['wind_speed']} m/s")

print()

print(f'Average wind, Lapland: {round(sum(wind_speeds_by_area["lapland"]) / len(wind_speeds_by_area["lapland"]), 1)} m/s')
print(f'Average wind, Middle part of Finland: {round(sum(wind_speeds_by_area["middle"]) / len(wind_speeds_by_area["middle"]), 1)} m/s')
print(f'Average wind, Southern Finland: {round(sum(wind_speeds_by_area["south"]) / len(wind_speeds_by_area["south"]), 1)} m/s')

