# Number Guessing Game

'''This is a game where the computer selects a random number between 1 and 100,
and the user guesses what that number is.  There are two difficulties.  Easy means you get five guesses and hard mode means you get ten guesses.  After each guess, the computer will tell you if your guess was higher or lower than the number.'''

from art import logo #ASCII Art
import random # random module for randint function

# introducing the game and choosing the difficulty level
print(logo)
print("\nWelcome to the Guess The Number Game!")
print("\nI am thinking of a number between 1 and 100....")
mode = input("\nDo you want to play on 'easy' or 'hard' mode?: ").lower()
print(f"\nOK, let's play on {mode} mode.")

# A function that is called to run the game.
def play_game(mode, ct=0):

  answer = random.randint(1, 101) # computer selects a random number

  game_over = False
  while game_over == False:
  
    number = int(input("\nEnter a number: ")) # user makes a guess
  
    if mode == "easy":
      num_of_guesses = 10 # easy mode gets 10 guesses
    elif mode == "hard":
      num_of_guesses = 5 # hard mode gets 5 guesses
    
    if number == answer:
      print(f"\nNice job, you won! The number was {number}.")
      game_over = True
    elif number > answer:
      print("Too high")
    elif number < answer:
      print("Too low")

    if game_over == False:
      ct += 1
      num_of_guesses = num_of_guesses - ct
      print(f"You have {num_of_guesses} guesses remaining.")
  
    if num_of_guesses == 0:
      print(f"\nYou ran out of guesses.  The number was {answer}.")
      game_over = True

play_game(mode, 0)
  
  