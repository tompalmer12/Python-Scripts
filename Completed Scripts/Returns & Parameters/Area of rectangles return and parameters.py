def main():
    r1 = int(input("Please enter rectangle width: "))
    r2 = int(input("Please enter rectangle height: "))

    result = area_rect(r1, r2)
    print("The area is", result)

def area_rect(w, h):
    return (w * h)

main()
