# This script will handle the user input front-end
def user_entry():
    global user_input
    try:
        user_input = str(input("Enter a keyword: "))

        if user_input.isspace() == False and user_input != "":
            print("Done!")

        if user_input == "":
            re_input_1 = str(input("Please enter a keyword: "))
            user_input = re_input_1
            print("Done!")

        if user_input.isspace() == True:
            re_input_2 = str(input("Please enter valid keyword: "))
            user_input = re_input_2
            print("Done!")

    except EOFError:
        user_input = str(input("Please enter a keyword:"))
        print("Done!")

    return user_input

user_entry()