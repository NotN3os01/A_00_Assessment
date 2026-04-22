import math
import random


symbol_list = ["+" , "-", "*", "/" ]
num1 = random.randint(1, 10,)
num2 = random.randint(1, 10)

# checks users enter yes (y) or no (n)


def int_check(question):
    while True:
        error= "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"


        try:
            response = int("Enter an integer: ")

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)



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


#Main Routine goes here



# Main Routine starts here

# Initialise game variables
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
num_rounds = int_check("How many rounds would you like <enter for infinite>: ")

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

    comp_choice = random.choice(symbol_list)



    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Show the math question which is the first number and the second number doing one of the four equations
    print(f"\nQuestion {rounds_played+1} of {num_rounds} : {num1} {comp_choice} {num2}")

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



