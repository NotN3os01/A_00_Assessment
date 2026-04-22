import math
import random

from Assessment.A_06_Math_Questions import answer

symbol_list = ["+" , "-", "*", "/" ]
num1 = random.randint(1, 10,)
num2 = random.randint(1, 10)


# checks users enter yes (y) or no (n)



def yes_no(question):
    while True:

        response = input(question).lower()

        # checks user response. question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions
def instructions():
    """Prints instructions"""

    print('''
**** Instructions ****

In this quiz, you will be answering multi-choice
questions and you may choose one out of the 
four options being (A, B, C, D). If you are incorrect,
you will be told the correct answer after and if you 
would like to quit at any point and time, use the exit 
code (xxx)

Good luck.

    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

# calculate the maximum number of guesses


    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")


    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            return response

        except ValueError:
            print()



# calculate the number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low +1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped +1
    return max_guesses

#Main Routine goes here



# Main Routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []


print("✖️➕➖➗ Welcome to the math quiz ➗➖➕✖️")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                   low=1, exit_code="")



if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# allow user to choose high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num+1)

# calc max number of guesses
guesses_allowed = calc_guesses(answer)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️ "
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Show the math question which is the first number and the second number doing one of the four equations
    print(f"\nQuestion {rounds_played+1} of {num_rounds} : {num1} {comp_choice} {num2}")

    comp_choice = answer
    z = comp_choice
    x = num1
    y = num2
    answer = eval(f"{x} {z} {y}")

    print(round(answer))

    # ask user for the answer
    user_choice = int_check(f"\n What is the answer?? ")
    # find out if the answer is correct or incorrect
    if user_choice == answer:
        print("You got this answer correct!")
        continue
    else:
        print("This answer is incorrect.")
        print(f"The answer was {answer}")

        if end_game == "yes":
            break



