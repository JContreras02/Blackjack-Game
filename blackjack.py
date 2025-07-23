import blackjack_art
import random

print(blackjack_art.logo)

# Deck of cards (cards will not be removed from the deck)
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function that uses the list to return a random card.
def deal_card():
    user_hand = []
    user_card1 = random.choice(deck)
    user_card2 = random.choice(deck)
    user_hand.extend([user_card1, user_card2])

    print(user_hand)
    print(sum(user_hand))

    computer_hand = []
    computer_card1 = random.choice(deck)
    computer_card2 = random.choice(deck)
    computer_hand.extend([computer_card1, computer_card2])

    print(computer_hand)
    print(sum(computer_hand))

deal_card()