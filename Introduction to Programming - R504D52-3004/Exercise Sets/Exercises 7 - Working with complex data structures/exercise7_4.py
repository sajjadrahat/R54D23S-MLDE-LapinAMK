movies_collection = [
    {"name": "Casablanca", "year": 1942},
    {"name": "Forrest Gump", "year": 1994},
    {"name": "Avatar", "year": 2009},
    {"name": "The Shawshank Redemption", "year": 1994},
    {"name": "Inception", "year": 2010},
    {"name": "The Godfather", "year": 1972},
    {"name": "Sisu", "year": 2023},
]

list_of_movies_after_2000=[]
list_of_movies_before_2000 =[]

for i in movies_collection:
    if i["year"] <= 2000:
        list_of_movies_before_2000.append(i["name"])
    else:
        list_of_movies_after_2000.append(i["name"])

   
print("These movies have been released in year 2000 or later:")
print(",".join(list_of_movies_after_2000))
print()
print("These movies have been released before the year 2000:")
print(", ".join(list_of_movies_before_2000))    