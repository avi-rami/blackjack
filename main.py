### Our Blackjack House Rules ###

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from clear import clear
import random

# returns a boolean for game loop
def game_choice():
  choice = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
  if choice == 'y':
    return True
  else:
    return False

# calculates score and chooses the optimal value for ace
def calculate_score(hand):
  score = 0
  for card in hand:
    score += card
    if 11 in hand and score > 21:
      hand.remove(11)
      hand.append(1)
      score -= 10
  return score

def compare_scores(u_score, c_score, is_bj):
  if user_score == computer_score:
    return "Draw 🙃"
  elif is_blackjack is True and user_score == 21:
    return "Win with a Blackjack 😎"
  elif is_blackjack is True and computer_score == 21:
    return "Lose, opponent has Blackjack 😱"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  elif user_score < computer_score:
    return "You lose 😤"

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = game_choice()  # initial user prompt
clear()

# main game while loop
while (play_game is True):
  print(logo)

  # initilaize variables and lists
  user_hand = []
  computer_hand = []
  user_score = 0
  computer_score = 0
  num_turns = 0
  is_blackjack = False

  # while loop for getting another card
  get_card = 'y'
  while (get_card == 'y' and user_score <= 21):
    # turn 0 - intializes both decks and breaks loop if a blackjack
    if num_turns == 0:
      for i in range(0, 2):
        user_hand.append(random.choice(cards))
        user_score = calculate_score(user_hand)  # 21
        computer_hand.append(random.choice(cards))
        computer_score = calculate_score(computer_hand)
      if user_score == 21 or computer_score == 21:
        is_blackjack = True
    elif num_turns > 0:
      # computer goes until score > 16
      while (computer_score < 17):
        computer_hand.append(random.choice(cards))
        computer_score = calculate_score(computer_hand)
      # user turn
      user_hand.append(random.choice(cards))
      user_score = calculate_score(user_hand)

    # displays hand, score, and dealer's 1st card as game runs
    print(f"  Your cards: {user_hand}, current_score: {user_score}")
    print(f"  Computer's first card: {computer_hand[0]}")

    # exit out of get_card loop if the player achieves blackjack
    if is_blackjack is True:
      break
    elif user_score > 21:
      break
    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    num_turns += 1  #increments the number of turns

  # display the final stats before showing win outcome
  print(f"  Your final hand: {user_hand}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_hand}, final score: {computer_score}")

  # display the winning/losing outcomes
  print(compare_scores(user_score, computer_score, is_blackjack))

  # prompts user to start another game
  play_game = game_choice()
  clear()