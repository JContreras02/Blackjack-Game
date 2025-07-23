import blackjack_art
import random

print(blackjack_art.logo)

# Function that returns a random card.
def deal_card():
    """Returns a random card from the deck"""

    # Deck of cards (cards will not be removed from the deck)
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card = random.choice(deck)
    return user_card

# Function that sums up the score
def calculate_score():
    """Function that takes the list of cards as input and returns the sum as a score."""
    return

user_hand = []
computer_hand = []

for _ in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())