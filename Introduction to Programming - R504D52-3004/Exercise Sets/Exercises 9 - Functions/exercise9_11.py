import functions

city_landmarks = [
    {"city": "Paris", "landmark": "Louvre Museum"},
    {"city": "London", "landmark": "National Gallery"},
    {"city": "Paris", "landmark": "Eiffel Tower"},
    {"city": "London", "landmark": "Madame Tussauds"},
    {"city": "London", "landmark": "British Museum"},
    {"city": "Paris", "landmark": "Notre Dame"}
]

# Getting sorted data using functions
sorted_city_landmarks = functions.city_landmark_sort(city_landmarks)

# Print sorted data
for data in sorted_city_landmarks:
    print(f"{data['city']} : {data['landmark']}")