import json


def load_products(data_location):
    with open(data_location, 'r') as json_data:
        products_data = json.load(json_data)
    return products_data


def print_product_list(data):
    print("\nProduct List:")
    for i, product in enumerate(data, start=1):
        print(f"{i} : {product['name']}, Category: {product['category']}, Price: {product['price']}")

def save_products(data_location, products_data):
    with open(data_location, 'w') as json_file:
        json.dump(products_data, json_file, indent=2)
def modify_products(data_location):
    load_data = load_products(data_location)
    print("\nChoose a product index to modify:")
    print_product_list(load_data)
    user_index= int(input("Choose: "))
    product_index = user_index -1
    product = load_data[user_index-1]
    print(f"{user_index} : {product['name']}, Category: {product['category']}, Price: {product['price']}")
    print("""What do you want to modify? :
                1. Name
                2. Category
                3. Price """)
    user_input= int(input("Choose: "))
    if user_input==1:
        print(f"Old Name: {product['name']}")
        modified_data = input("New Name: ")
        load_data[product_index]['name'] = modified_data
    elif user_input==2:
        print(f"Old Category: {product['category']}")
        modified_data = input("New Category: ")
        load_data[product_index]['name'] = modified_data
    elif user_input==3:
        print(f"Old Price: {product['price']}")
        modified_data = float(input("New Price: "))
        load_data[product_index]['name'] = modified_data
    else:
        return None

    print("Product data modified Successfully. \n")
    with open(data_location, 'w') as json_file:
        json.dump(load_data, json_file, indent=2)



def add_products(data_location):
    print("Add a new product")
    load_data = load_products(data_location)
    new_name= input("Name: ")
    new_category = input("Category: ")
    new_price = round(float(input("Price: ")), 2)
    new_data= {'name': new_name,
               'category': new_category,
               'price': new_price}
    load_data.append(new_data)
    with open(data_location, 'w') as json_file:
        json.dump(load_data, json_file, indent=2)

def delete_products(data_location):
    print("Choose a product index you want to delete: ")
    load_data = load_products(data_location)
    print_product_list(load_data)
    user_input = int(input('Choose: '))
    product_index = user_input-1
    product = load_data[product_index - 1]
    print(f"{product_index} : {product['name']}, Category: {product['category']}, Price: {product['price']}")

    load_data.pop(product_index)
    print(f"Products deleted successfully!")
    with open(data_location, 'w') as json_file:
        json.dump(load_data, json_file, indent=2)


data_location = 'product.json'
while True:
    products_data = load_products(data_location)
    print_product_list(products_data)
    print("\nOptions:")
    print("1. Modify a product")
    print("2. Add a new product")
    print("3. Delete a product")
    print("4. Quit \n")
    user_input= int(input("Choose an option: "))

    if user_input==1:
        modify_products(data_location)
    elif user_input==2:
        add_products(data_location)
    elif user_input==3:
        delete_products(data_location)
    elif user_input==4:
        break

