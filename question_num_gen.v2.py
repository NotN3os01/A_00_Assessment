import math
import random

def int_check(question):
    while True:
        error= "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"


        try:
            response = int(input("Enter an integer: "))

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

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

    ''')

# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

#Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()
print()



num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
symbol_list = ('*', '+', '/', '-')
comp_choice = random.choice(symbol_list)

# Show the math question which is the first number and the second number doing one of the four equations
print(f"\nQuestion X : {num1} {comp_choice} {num2}")
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


