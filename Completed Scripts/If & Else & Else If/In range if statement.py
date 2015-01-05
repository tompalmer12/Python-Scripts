def main():
    print(in_range(4, 1, 10))            # prints "True",  4  is in 1 to 10
    print(in_range(1, 1, 10))            # prints "True",  1  is in 1 to 10
    print(in_range(0, 1, 10))            # prints "False", 0 not in 1 to 10
    print(in_range(5, 1, 5))             # prints "True",  5  is in 1 to  5

def in_range(val, lo, hi):
    return True if val >= lo and val <= hi else False

main()


