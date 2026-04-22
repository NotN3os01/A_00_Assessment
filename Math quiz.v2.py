import math
import random

from Assessment.A_04_Integer_Checker_v1 import rounds_heading

symbol_list = ["+" , "-", "*", "/" ]
num1 = random.randint(1, 10,)
num2 = random.randint(1, 10)



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

In this quiz, you will be answering single answer
questions and you will be asked a question on mathematics.
If you are incorrect, you will be told the correct answer
after the answer was incorrect. However, if the answer is correct,
you may experience the joy from success and if you 
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
num_rounds = int_check("Rounds <enter for infinite> or any number for rounds: ",
                   low=1, exit_code="")



if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# allow user to choose high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num+1)


# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️ "
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)


    comp_choice = random.choice(symbol_list)



    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Round starts here
    # Set guesses used to zero at the start of each round
    # Show the math question which is the first number and the second number doing one of the four equations
    print(f"\nQuestion {rounds_played + 1} of {num_rounds} : {num1} {comp_choice} {num2}")

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
    else:
        print("This answer is incorrect.")
        print(f"The answer was {answer}")
        print(rounds_heading)


    print()

    # Round ends here

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break

    # Add round results to game history
    history_feedback = f"Round {rounds_played}: {feedback}"

    game_history.append(history_feedback)

    rounds_played += 1
    all_scores.append(guesses_used)

# check users have played at least one round
# before calculating stats.
if rounds_played > 0:

    # Game history / statistics area

    # calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Best:{best_score} | Worst:{worst_score} | Average: {average_score:.2f} ")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)
            print()




