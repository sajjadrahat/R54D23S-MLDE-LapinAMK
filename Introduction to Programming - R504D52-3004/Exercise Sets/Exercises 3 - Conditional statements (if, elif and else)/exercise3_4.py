customer_money = int(input("Give money: \n"))
purchase_cost = int(input("Purchase cost: \n"))

if customer_money == purchase_cost:
    print("Thank you")
elif customer_money > purchase_cost:
    change = customer_money - purchase_cost
    print(f"Thank you. Here is the change: {change}€")
else:
    extra_money = int(input("Not enough money, give more: \n"))

    if customer_money + extra_money == purchase_cost:
        print("Thank you")
    elif customer_money + extra_money > purchase_cost:
        change = customer_money + extra_money - purchase_cost
        print(f"Thank you. Here is the change: {change}€")
    else:
        print("You don't have enough money.")
