# Check if user would like to see the instructions with Yes/Y or No/N
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

    ''')

# Main routine
print()
print("✖️➕➖➗ Welcome to the math quiz ➗➖➕✖️ ")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")