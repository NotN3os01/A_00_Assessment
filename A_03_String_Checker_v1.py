# Check that users have entered a valid
# option based on a list
def string_checker(user_response, valid_ans):
    while True:


       # Get user response and make sure it's lowercase
        user_response = user_response.lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"
