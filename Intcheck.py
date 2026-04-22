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