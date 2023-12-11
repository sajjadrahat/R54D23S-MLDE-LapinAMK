import functions

serial_test_csv = 'serialtest.csv'

# Read and print the data
original_data = functions.read_csv(serial_test_csv)
print("Original CSV file:")
functions.print_csv(original_data)

# Increase everyone's salary by 100 €
functions.increase_salary(original_data)
new_csv = 'new_serialtest.csv'
functions.save_csv(new_csv, original_data)

print("\nNew CSV file:")
functions.print_csv(original_data)