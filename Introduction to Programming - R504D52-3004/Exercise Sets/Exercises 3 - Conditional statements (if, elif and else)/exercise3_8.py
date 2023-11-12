sum_cost = int(input("Total cost of the order: "))
student=input("Are you student? Reply with 'Y' or 'N': ")
vip_customer=input("Are you vip customer? Reply with 'Y' or 'N': ")

total_cost=sum_cost
if vip_customer=="Y":
    points=int(input("How many points do you have from previous purchases?: "))
sales_code=input("Do you have any special sales code? if not type 'N': ")
sales_codes_dict={"FALL23":0.10,"BK2SCHOOL":0.20}

if sales_code in sales_codes_dict and (student == "Y" or vip_customer == "Y"):
    total_cost -= total_cost * sales_codes_dict[sales_code]
if vip_customer=="Y":
    points+=round((total_cost-(total_cost%10))/10)*100
    total_cost-=round(points/1000)*5
if total_cost<=99:
    total_cost+=7.95
print(f"You need to pay: {round(total_cost,2)} €")