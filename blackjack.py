from blackjack_art import logo
import random

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
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if (11 in cards) and (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Function that checks scores to decide winner
def compare(u_score, cpu_score):
    """Function that takes user score and computer score as input to decide on the winner."""
    if u_score == cpu_score:
        return "Draw!"
    elif cpu_score == 0:
        return "You Lose... Opponent has a blackjack!"
    elif u_score == 0:
        return "You Win!!! You have a blackjack!"
    elif u_score > 21:
        return "You Lose... You went over!"
    elif cpu_score > 21:
        return "You Win! Opponent went over!"
    elif u_score > cpu_score:
        return "You Win!!!"
    else:
        return "You Lose..."

# Function that runs entire blackjack name until user types 'n'.
def play_game():
    """Funtion to run Blackjack game."""

    print(logo)
    user_hand = []
    computer_hand = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
            user_hand.append(deal_card())
            computer_hand.append(deal_card())

    # Loop that runs until user no longer wants more cards.
    while not is_game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            keep_playing = input(f"Type 'y' to get another card, type 'n' to pass: ")
            print("\n")
            if keep_playing == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True

    # Loop that checks for blackjack and makes sure cpu has a score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand is: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand is: {computer_hand}, final score: {computer_score} \n")
    print(compare(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()