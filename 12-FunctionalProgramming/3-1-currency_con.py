def main():
    euro = [15.90, 38.47, 4.07, 132.70, 9.15]

    to_pln = list(map(lambda x:x*4.5, euro))

    print(to_pln)
    for i in to_pln:
        print(i)

if __name__ == "__main__":
    main()