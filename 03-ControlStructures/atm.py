###
# ATM (cash machine) simulator
#addition
#
balance = 1000  # Initial balance
true_pin = "1234"
pin = input('enter the pin') # initial 4-digit PIN code
Check = False
check2 = False

if pin.isdigit == True and len(pin) == 4:
    check = True

while check == True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. change pin")
    print("5. Exit")


    choice = input("Choose an option (1-4): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == "4":
        while check2 == False:
            true_pin = input("enter new pin: ")
            if pin.isdigit == True and len(pin) == 4:
                print("New pin saved and valid")
                check2 = True
            else:
                print("Invalid pin")
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
