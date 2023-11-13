import statistics
student_grades=[]
grades_description={"Bad result":[0,1],"Weak result":[1,2],"Average result":[2,3],"Good result":[3,4],"Excellent result":[4,5]}
students_count = int(input("How many students? \n"))
for i in range(students_count):
    student_grades.append(int(input("Student grade: \n")))
avg= round(statistics.mean(student_grades), 2)
median = round(statistics.median(student_grades), 2)
mode = round(statistics.mode(student_grades), 2)
print(f"Average grade: {avg}")
for val, keys in grades_description.items():
    if keys[0] <= avg <keys[1]:
        print(val)
        break
print(f"Median grade: {median}")
print(f"Mode grade: {mode}")