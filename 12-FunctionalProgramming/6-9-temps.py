def main():
    teps = {
        "Krakow":7,
        "Warszawa":-2,
        "Sopot":4,
        "Koszalin":-1,
        "Opole":3
    }

    positive = filter(lambda city: teps[city]>0, teps)

    print("city with positive temperature:")
    for city in positive:
        print(city, end = ' ')
if __name__ == "__main__":
    main()