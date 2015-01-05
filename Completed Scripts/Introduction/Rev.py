number = int(input("Please enter a 3 digit number: "))

hundreds = number // 100
tens = (number % 100) // 10
units = number % 10

print(units,tens,hundreds)



