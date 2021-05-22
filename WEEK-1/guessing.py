import random
random_number = random.randint(1, 10)
while True:
    guess = input("Pick a number from 1 to 10")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH")
    else:
        print("YOU WIN!")
# Black Jack game


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

    user_cards = []
    computer_cards = []
