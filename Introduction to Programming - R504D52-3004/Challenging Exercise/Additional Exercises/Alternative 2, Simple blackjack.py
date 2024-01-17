import random

card_values = {
    1: 'Ace',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}
def card_generator():
    return random.randint(1, 13)


user_balance = float(input("Balance: \n"))
user_cards = [card_generator(), card_generator()]
computer_cards = [card_generator()]

while True:
    print(f"Current balance: {user_balance}")
    betting_amount= float(input("Enter betting amount: \n"))

    print(f"Your current cards= {user_cards} and current sum= {sum(user_cards)}", end="")

    if sum(user_cards) == 21:
            print("BLACKJACK! PLAYER WINS")
            user_balance+=betting_amount
            break
    elif sum(user_cards) > 21:
            print("HOUSE WINS")
            user_balance+=betting_amount
            break
    
    game = input("Type 'y' to get another card, 'n' to end the game: ")

    if game == 'y':
            user_cards.append(card_generator())
    elif game == 'n':
            break
while sum(computer_cards) < 17:
        computer_cards.append(card_generator())

print(f"Your final cards: {user_cards}, final sum: {sum(user_cards)}")
print(f"Computer's final cards: {computer_cards}, final sum: {sum(computer_cards)}")

if sum(user_cards) <= 21 and (sum(computer_cards) > 21 or sum(user_cards) > sum(computer_cards)):
        print("PLAYER WINS!")
else:
        print("HOUSE WINS!")
