monthly_salary= float(input("Your monthly salary: \n"))
tax_perchantage = float(input("Your tax perchantage:\n"))
tax_money=round(monthly_salary*tax_perchantage/100,2)
print(f"Earnings: {monthly_salary-tax_money} €\nTaxes: {tax_money} €")