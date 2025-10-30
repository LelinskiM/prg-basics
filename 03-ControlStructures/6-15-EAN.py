EAN = input("Enter the EAN code: ")
if len(EAN) != 13 or not EAN.isdigit():
    print("Invalid EAN code. It must be a 13-digit number.")
else:
    print("Valid EAN code.")
    if EAN.startswith("590"):
        print("This EAN code is from Poland.")