import random
# checks for integers less than zero for the rounds component
# if the choice is less than zero
def int_check(question, num=None, exit_code=None):
    # if any integer is allowed...
    if num is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'number')
    elif num is not None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {num}")

    # check that the integer the user entered has a greater value than the variable 'num'
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
            print(error)

# checks if the user would like instructions or not with a simple yes/no checker
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

# print the instructions on request
def instructions():
    """Prints instructions"""

    print('''
**** Instructions ****

Welcome to the math quiz, here you will need
to answer math questions and if you are correct,
it will say you were correct and if you were wrong,
it will show you the answer and say that you were 
incorrect. Your job is the get as many answers correct
as possible and if you would like to finish at any time,
please enter the exit code 'xxx'.

Good Luck.

    ''')

# check if the integer the user entered is more than the variable 'num'
def num_check(question, num_type=int, num=0, exit_code="xxx"):
    error = f"Please enter an integer that is more than {num}."

    while True:
        # Ask user question and return response of
        # exit code is returned
        response = input(question)
        if response == exit_code:
            return response

        # Check response is more than minimum
        try:
            response = num_type(response)

            if response > num:
                return response
            else:
                print(error)

            # Show error if response is invalid
        except ValueError:
                print(error)

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

# Ask user for number of rounds / infinite mode
num_rounds = num_check("Rounds <enter for infinite>: ",
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

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol_list = ('+', '*', '-')
    comp_choice = random.choice(symbol_list)
    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1
    rounds_played += 1
    z = comp_choice
    x = num1
    y = num2
    error = f"Please enter an integer"
    # print the question that the user has to answer
    print(f"\nQuestion {rounds_played} : {num1} {comp_choice} {num2}")
    answer = eval(f"{x} {z} {y}")
    # ask user to use an integer if their answer is not an integer
    user_choice = int_check(f"\nWhat is the answer?? ", exit_code="xxx")
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

    # print feedback to user
    print(feedback)
# Game loop ends here
# Game history / statistics area
    # Add round results to game history
    history_feedback = f"Round {rounds_played}: {feedback}"

    game_history.append(history_feedback)

    all_scores.append(num_rounds)
if rounds_played > 0:
    # Calculate the percentage of correct and incorrect answers
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




