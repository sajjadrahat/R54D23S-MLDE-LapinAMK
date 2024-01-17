import csv

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]
    return data

def print_csv(data):
    for row in data:
        print(', '.join(row))

def increase_salary(data):
    # Row 1 is header, so loop is going to be run after first row
    for row in data[1:]:
            # Salary in last column
            # Getting the salary and converting to int
            current_salary = int(row[4])
            new_salary = current_salary + 100
            row[4] = str(new_salary)

def save_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

serial_test_csv = 'serialtest.csv'

# Read and print the data
original_data = read_csv(serial_test_csv)
print("Original CSV file:")
print_csv(original_data)

# Increase everyone's salary by 100 €
increase_salary(original_data)
new_csv = 'new_serialtest.csv'
save_csv(new_csv, original_data)

print("\nNew CSV file:")
print_csv(original_data)