def main():
    name = get_data()
    display_greeting(name)

def get_data():

    # ask the user for their name & returns data to main
    return input("Please enter your name: ")

def display_greeting(name):
    #prints hello and data from variable "name"
    print("Hello " + name)


# runs the main function
main()
