car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
###
# Bubble sort
#
def bubble_sort(n):

   for i in range(len(n)):
      for j in range(len(n)):
         if n[i] < n[j]:
            n[i], n[j] = n[j], n[i]

   return n

print(bubble_sort(car_fuel_consumption))
print(bubble_sort(bank_transactions))  
print(sorted(car_fuel_consumption))
print(sorted(bank_transactions, reverse=True))