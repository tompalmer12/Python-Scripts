def main():
    number = int(input("Enter base number for multiplication table:"))

    print(mult_table(number, 1))
    print(mult_table(number, 2))
    print(mult_table(number, 3))
    # .......... etc ..........
    print(mult_table(number, 10))
    print(mult_table(number, 11))
    print(mult_table(number, 12))


def mult_table(base, multiplier):
    return str(base) + " * " + str(multiplier) + " = " + str(base*multiplier)


main()