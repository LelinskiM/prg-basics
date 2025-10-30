Num_Of_Products = int(input("Enter the number of products you want to buy: "))
Product_Price = int(input("Enter the price of the product: "))
Total_Cost = 0
if Num_Of_Products > 2:
    Total_Cost += (Product_Price*2)
    Num_Of_Products -= 2
    while Num_Of_Products > 0:
        Total_Cost += (Product_Price*0.75)
        Num_Of_Products -= 1 
else:
    Total_Cost += (Product_Price*Num_Of_Products)
print("The total cost of your purchase is: ", Total_Cost,"zł")
