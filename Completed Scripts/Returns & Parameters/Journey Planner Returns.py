def main():
    destination, distance = get_travel_data()

    drive_time = distance / 60

    print("From Sheffield to", destination, "it is", distance, "miles")
    print("In a car it'll take around", drive_time, "hours")


def get_travel_data():

    destination = input("Where ya going? ")
    distance = int(input("How far's that? "))

    return destination, distance

main()
