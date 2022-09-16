import random
from replit import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and len(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It is a draw"
    elif computer_score == 0:
        return "You lose! opponent has BlackJack"
    elif user_score == 0:
        return "You win! You have BlackJack"
    elif user_score > 21:
        return "You scored over! You lose!"
    elif computer_score > 21:
        return "Oppenent scored over! You Win!"
    elif user_score > computer_score:
        return "You Win!!!!!!"
    else:
        return "You lose!!!!!!!!"


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    game_ended = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and Current_score: {user_score}")
        print(f"Computer First Card: {computer_cards[0]}")
        is_continue = input(
            "Do you want draw another card? If yes then Type 'y' and if no then type 'n': "
        ).lower()
        if is_continue == "y":
            user_cards.append(deal_card())
        else:
            game_ended = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final cards: {user_cards} and Final score: {user_score}")
    print(
        f"  computer final cards: {computer_cards} and final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input("Do you wanna play the gmae BlackJack? type 'y' or 'n': ").lower(
) == "y":
    clear()
    blackjack()
