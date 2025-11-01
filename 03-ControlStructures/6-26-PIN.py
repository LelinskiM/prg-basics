PIN = "0805"
user_input = input("Enter your PIN: ")
count = 0
while count < 3:
    if user_input == PIN:
        print("PIN accepted. Access granted.")
        break
    else:
        count += 1
        if count < 3:
            user_input = input("Incorrect PIN. Try again: ")
        else:
            print("Sorry, your payment card has been blocked")