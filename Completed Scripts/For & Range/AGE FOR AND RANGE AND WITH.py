def main():
    age = get_age()

def get_age():
    age = int(input("Please enter your age: "))
    while age < 1 or age > 120:
        print("Error! Must be between 1 and 120")
        ask = int(input("Please enter again: "))

    return age

main()

