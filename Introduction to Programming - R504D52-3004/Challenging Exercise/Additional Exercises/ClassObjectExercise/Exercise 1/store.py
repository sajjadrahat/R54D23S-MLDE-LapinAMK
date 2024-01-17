from product import Product
import random



products = [
        Product("Smart TV", "Electronics", 699.0, None),
        Product("Refrigerator", "Appliances", 799.0, "Cristmas"),
        Product("Headphones", "Audio", 79.9, None),
        Product("Digital Camera", "Electronics", 299.0, "Cristmas"),
        Product("Toaster", "Appliances", 29.9, None),
    ]

print("Product Details:")
for p in products:
        p.print_info()

print("Product Prices:")
for p in products:
    print(f"{p.name} Price: {p.get_price()}€")

sorted_products = sorted(products, key= lambda x: x.category)
print("\nSorted Products:")
for p in sorted_products:
    p.print_info()