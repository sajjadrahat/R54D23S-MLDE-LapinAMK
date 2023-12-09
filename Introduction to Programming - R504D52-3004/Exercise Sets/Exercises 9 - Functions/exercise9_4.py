import functions

# ask all the names as one string from user
# Example Names: James Smith, Maria Garcia, George Wilson, Sarah Miller, Jane Davis
people_string = input("Write all participants, separated by a comma:\n")
# convert the text into a list
people = people_string.split(",")
# remove extra space-characters from each name (from the beginning and end)
people = [p.strip() for p in people]
# the people-variable now is a list, that contains full names of each participant

# 1. Print the list in original order
functions.show_numbered_list("Original order:", people)

# 2. Sort the list into alphabetical order by first name
people.sort()
functions.show_numbered_list("Alphabetic order by first name:", people)



# let's convert the people in the list so, that last name
# comes before the first name
# this is called "list comprehension" – a feature in Python
# The logic: each name will be split in its turn, and converted to a
# list based on the space character. Because of this, each full name will
# be a list of two elements: first name and the last name.
# After this, the order of the elements is changed by using the reverse-
# function. Finally, the two elements will be built back into a string by
# using the join() –function. The end result is a list that contains the
# full names of all people, but in the format of Last Name First Name

people = [" ".join(reversed(p.split(" "))) for p in people]

# 3. Sort the list into alphabetical order by last name
people.sort()
functions.show_numbered_list("Alphabetic order by last name:", people)