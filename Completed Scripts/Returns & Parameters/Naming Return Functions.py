def main():
    # call the function to set name
    name = get_name()

    # display the message
    print("Whaddup,", name, "?!")

def get_name():

    # asks the user for their name and returns it as a variable in main()
    ans = input("Please enter your name: ")
    return ans


# run the main function
main()
