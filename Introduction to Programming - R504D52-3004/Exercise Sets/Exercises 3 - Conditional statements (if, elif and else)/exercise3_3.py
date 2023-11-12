workhours = float(input("How many workhours this week? \n"))
hourly_salary = float(input("Your hourly salary? \n"))
if workhours>40:
    salary= round(40*hourly_salary+ (workhours-40)*(hourly_salary + 0.50*hourly_salary),2)
    print(f"Your weekly wage: {salary}€")
elif workhours<=40:
    salary = round(workhours*hourly_salary,2)
    print(f"Your weekly wage: {salary}€")