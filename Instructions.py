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
