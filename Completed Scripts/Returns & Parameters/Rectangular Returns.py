def main():
    width, height = get_rect_data()
    area = width * height
    print("The area is", area)

def get_rect_data():
    width = int(input("Please enter width: "))
    height = int(input("Please Enter Height: "))

    return width, height



main()