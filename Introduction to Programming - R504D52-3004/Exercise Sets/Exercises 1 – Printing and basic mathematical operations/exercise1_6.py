amount_of_money = int(input("How many cents? (1-100): \n"))
coin_values = [50, 20, 10, 5, 2, 1]

for coin in coin_values:
    num_coins = amount_of_money // coin
    amount_of_money -= coin * num_coins
    print(f"Amount of {coin} in cents: {num_coins}")