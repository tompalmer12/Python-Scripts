def main():


    n1 = int(input("Enter the 1st number:"))
    n2 = int(input("Enter the 2nd number:"))
    n3 = int(input("Enter the 3rd number:"))

    biggest = find_largest(n1, n2, n3)

    print("The largest value is", biggest)

def find_largest(n1, n2, n3):


    if n1 >= n2:
        if n1 >= n3:
            return n1
        else: # this else must mean n3 > n1
            return n3
    else: # this else must mean n2 > n1
        if n2 >= n3:
            return n2
        else: # this else must mean n3 > n2
            return n3



main()