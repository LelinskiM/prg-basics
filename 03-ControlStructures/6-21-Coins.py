amount = int(input("Enter the amount in zł: "))
coins_5zl = amount // 5
remaining_amount = amount % 5
coins_2zl = remaining_amount // 2
remaining_amount = remaining_amount % 2
coins_1zl = remaining_amount   

print(f"The minimum number of coins needed for {amount} zł:")
print(f"Number of 5 zł coins: {coins_5zl}")
print(f"Number of 2 zł coins: {coins_2zl}")
print(f"Number of 1 zł coins: {coins_1zl}")