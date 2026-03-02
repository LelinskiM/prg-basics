class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance: {self.distance} km")
        print(f"Rate per km: €{self.rate_per_km}")
        print(f"Total fare: €{self.fare}")
        print("-" * 20)


def main():
    # your program
    Ride1 = TaxiRide(2)
    Ride1.distance = 10
    Ride1.calculate_fare(Ride1.distance)
    ride2 = TaxiRide(3)
    ride2.distance = 15
    ride2.calculate_fare(ride2.distance)

    Ride1.print_receipt()
    ride2.print_receipt()


if __name__ == "__main__":
    main()
