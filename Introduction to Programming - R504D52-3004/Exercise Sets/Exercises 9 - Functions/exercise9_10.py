import random

# lambda that returns a Boolean depending on whether the given integer is even
even_check = lambda x: x % 2 == 0

# Create a collection with a random number of both odd and even numbers
# Using list comprehension
random_numbers = [random.randint(1, 100) for i in range(random.randint(5, 15))]


#filter() function to filter out the collection using the lambda and create a new list
filter_odd = list(filter(lambda x: not even_check(x), random_numbers))
#map() function to filter out the collection using the lambda and create a new list
map_even= list(map(even_check, random_numbers))

# Print the lists on the screen
print("Random Numbers:", random_numbers)
print("Filtered Odd Numbers:", filter_odd)
print("Boolean Values for Even Numbers:", map_even)