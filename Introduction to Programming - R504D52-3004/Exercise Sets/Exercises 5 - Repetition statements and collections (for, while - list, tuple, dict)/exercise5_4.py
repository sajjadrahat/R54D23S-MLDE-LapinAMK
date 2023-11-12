city_list=["Rome", "Athens", "Stockholm", "London", "Dublin", "Paris"]
city_list.sort()
for i in range(1,len(city_list)+1):
    print(f"{i}: {city_list[i-1]}")