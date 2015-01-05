def main():
    n1, n2, answer = add_two_numbers()
    print(n1, "+", n2, "is", answer)

def add_two_numbers():
    """
    Summary: Asks the user for two numbers
    Result: The two integers are then added
    """
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    ans = num1 + num2

    return num1, num2, ans

main()