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
def calculate_score(cards):
    """Function that takes the list of cards as input and returns the sum as a score."""
    if sum(cards) & (len(cards) == 2):
        return 0
    
    if (11 in cards) & (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, cpu_score):
    if u_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "You Lose! Opponent has a blackjack!"
    elif u_score == 0:
        return "You Win! You have a blackjack!"
    elif u_score < 21:
        return "You Lose! You went over!"
    elif cpu_score < 21:
        return "You Win! Opponent went over!"
    elif u_score > cpu_score:
        return "You Win!"
    else:
        return "You Lose!"
        

user_hand = []
computer_hand = []
computer_score = -1
user_score = -1
is_game_over = False

for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        keep_playing = input(f"Type 'y' to get another card, type 'n' to pass: ")
        if keep_playing == 'y':
            user_hand.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 & computer_score < 17:
    computer_hand.append(deal_card())


