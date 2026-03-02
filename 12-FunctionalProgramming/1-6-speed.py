def avarage_speed(distance, hours, min):
    total_time = hours + min/60
    return distance/total_time

def main():
    distance = float(input("Enter the distance in kilometers: "))
    hours = int(input("Enter the hours: "))
    min = int(input("Enter the minutes: "))
    print(f"Average speed: {avarage_speed(distance, hours, min)} km/h")

if __name__ == "__main__":
    main()