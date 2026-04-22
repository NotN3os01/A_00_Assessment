import random
import math


# checks for integers less than zero
def int_check(question, num=None, exit_code=None):
    # calculate the maximum number of guesses

    # if any integer is allowed...
    if num is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif num is not None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {num}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that is "
                 f"greater than {num}")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low...
            if num is not None and response < num:
                print(error)
            # if response is valid, return it
            return response

        except ValueError:
            print()


def yes_no(question):
    """Checks user response to a question is yes / no (y/n) returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print('''
**** Instructions ****

Welcome to the math quiz, here you will need
to answer math questions and if you are correct,
it will say you were correct and if you were wrong,
it will show you the answer and say that you were 
incorrect. Your job is to get as many right as possible
and watch out because you only get one chance to answer correctly.
If you want to quit anytime, you will be asked if you would like to quit.

    ''')


def string_checker(valid_ans=("yes", "no", "xxx")):
    error = f"Please enter a valid option form the following list: {valid_ans - 1}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(valid_ans).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Main Routine starts here
# Initialise game variables
mode = "regular"
rounds_played = 0
game_history = []
all_scores = []
rounds_correct = 0
rounds_incorrect = 0
end_game = "no"
feedback = ""

print("✖️➕➖➗ Welcome to the math quiz ➗➖➕✖️")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       num=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️ "
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    rounds_played += 1
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol_list = ('+', '*', '-')
    comp_choice = random.choice(symbol_list)
    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    z = comp_choice
    x = num1
    y = num2

    print(f"\nQuestion {rounds_played} : {num1} {comp_choice} {num2}")
    answer = eval(f"{x} {z} {y}")
    print(round(answer))
    # ask user for the answer
    user_choice = int_check(f"\n What is the answer??", exit_code="xxx")
    if user_choice == "xxx":
        break
    # find out if the answer is correct or incorrect
    if user_choice == answer:
        rounds_correct += 1
        feedback = f"You got this answer correct!"
    else:
        feedback = f"This answer is incorrect."
        rounds_incorrect += 1
        print(f"The answer was {answer}")
        # ask the user to guess the number...

    # print feedback to user
    print(feedback)

# Game loop ends here

# Game history / statistics area

if rounds_played > 0:
    # Calculate Statistics
    rounds_correct = rounds_played - rounds_incorrect
    rounds_incorrect = rounds_played - rounds_correct
    percent_won = rounds_correct / rounds_played * 100
    percent_lost = rounds_incorrect / rounds_played * 100

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f}% \t "
          f"😢 Lost: {percent_lost:.2f}% \t")

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)
            print()

    print()
    print("Thanks for playing")

# Game history / statistics area





