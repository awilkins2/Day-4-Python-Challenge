# This imports the random library, which makes this entire program possible.
import random

# The input asks the user for their name, and the input is stored into the "name" variable.
name = input("What is your name? ")

# random.randint picks out a random digit between 1,100 (based on the given parameters), which
# is later assigned to the "randomnumber" variable.
randomnumber = random.randint(1, 100)

# The variable "number_of_tries" is capped at 8, shutting down the funtion loop after the
#player surpasses the limit.
number_of_tries = 0

# The print function here prints out the generic rules to play the game, as well as it
# incrporates the name variable to display the player's name.
print(
    "Well", name,
    "I've thought of a number between 1 and 100 and you only have 8 tries to guess it. What number do you think it is?"
)
# This input asks the user to input their numerical guess between 1 and 100, and that is stored
# in the variable "guess".
guess = int(input("What is your guess? "))

# This while loop repeats the guessing process until the player guesses the correct number, and
# until then, it will be terminated at the end of the 8th and final try.

for i in range(8):
  #This if statement checks if the player's guess is equal to the random number, and if it is,
  # the player wins the game.
  if guess < 1 or guess > 100:
    print("You have choosen a number out of play")
    guess = int(input("Can you select another number? "))
    number_tries = number_of_tries + 1
  # This elif statement checks if the player's guess is lower than the secret number, and if it
  # is, the statement is executed.
  elif guess < randomnumber:
    print("You have choosen a number lower than the secret number")
    guess = int(input("Can you select another number? "))
    number_of_tries = number_of_tries + 1
  # This elif statement checks if the player's guess is higher than the secret statement
  # If it is true, it is executed
  elif guess > randomnumber:
    print("You have choosen a number higher than the secret number")
    guess = int(input("Can you select another number? "))
    number_of_tries = number_of_tries + 1
  # This elif statement checks if the player's guess is equal to the secret number, and if it is
  # The statement prints out congradulations, and the number of tries it took the player to 
  # guess
  elif guess == randomnumber:
    number_of_tries = number_of_tries + 1
    print(
        f"Congrats {name} You have guessed the number correctly in {number_of_tries} tries"
    )
    break
else:
  print('You have run out of tries.')
# If none of the elif statements end up being true, this else statement will be triggered
# by default, since the player ran out of tries.