def main():
    num = int(input("Please enter a number: "))

    print("Before", num)

    num = multiplier(num)

    print("After ", num)

def multiplier(num, mult = 2):
    return num * mult

main()
