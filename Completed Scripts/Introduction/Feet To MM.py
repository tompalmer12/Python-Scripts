foot = 12

inch = 2.54

usr_foot = int(input("Please enter measurement in feet: "))
usr_inch = int(input("Please enter measurement in inches: "))

answer = ((usr_foot * foot) + usr_inch) * inch * 10

print(answer)