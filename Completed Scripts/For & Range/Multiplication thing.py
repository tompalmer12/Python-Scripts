def main():
    carry_on = "y"
    while carry_on == "y":
        base = int(input("Enter Number: "))
        mult = int(input("To the power of: "))
        result = power(base, mult)
        print(base," to the power of ",mult," is ",result)
        carry_on = input("Tryanother?(y/n)").lower()

def power(num1, num2):
    result = 1

    for counter in range(num2):
        result = result * num1

    return result

main()