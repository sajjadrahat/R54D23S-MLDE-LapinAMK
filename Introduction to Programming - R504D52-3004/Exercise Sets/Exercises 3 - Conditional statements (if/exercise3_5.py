points= int(input("Exam points: \n"))
#Using a dictionary to store the grades range values so that I don't need to write so many if statements.
grade_dict={0:[0,50], 1:[51,60], 2:[61,70],3:[71,80], 4:[81,90], 5:[91,100]}
for grade, grade_range in grade_dict.items():
    if points>= grade_range[0] and points<=grade_range[1]:
        print(f"Grade: {grade}")
        exit()
print("Invalid points value.")