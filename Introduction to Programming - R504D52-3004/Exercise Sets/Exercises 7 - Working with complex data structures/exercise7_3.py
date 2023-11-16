shopcart = [
 {"name": "Beehive - lamp", "price": 999.9},
 {"name": "Malm - bed", "price": 169.9},
 {"name": "Moomin - mug set", "price": 59.9},
 {"name": "Nemo - divan", "price": 699.9},
 {"name": "Ritz - armchair", "price": 369.9}
]
total_price=0
print("Reciept:")
for i in shopcart:
    print(f' - {i["name"]}')
    total_price+=i["price"]
print()
print(f"Total sum: {total_price}€.")
print("Please come again!")
vat = round(total_price/1.24,2)
print(f"Total vat: {vat}€.")
