Current_Price = float(input("Enter the current price of the item: "))
previous_Price = float(input("Enter the previous price of the item: "))
Discount = (previous_Price-Current_Price)/previous_Price
print(Discount)

if Discount >= 0.10:
    print("previous price: ",previous_Price)
    print("current price: ",Current_Price)
    print("The item is on sale by ", Discount*100,"%")
else:
    print("The item is not on sale.")   