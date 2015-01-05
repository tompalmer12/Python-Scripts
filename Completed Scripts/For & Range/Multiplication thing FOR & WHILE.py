def main():
    carry_on = "y"
    while carry_on != "n":
        base = int(input("Enter 1st number:"))
        mult = int(input("Enter 2nd number:"))
        result = multiply2(base, mult)
        print(base,"*",mult,"=",result)
        carry_on = input("Tryanother?(y/n)").lower()

def multiply(num1, num2):
    result = 0

    for counter in range(num2):
        result = result + num1

    return result

main()