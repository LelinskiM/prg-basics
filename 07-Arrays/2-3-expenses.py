# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]


# Calculates expenses
# Use loop statements

food = 0
transport = 0
utilities = 0
week1 = 0
week2 = 0
week3 = 0
week4 = 0

for r in range(len(monthly_expenses)):
    for c in range(len(monthly_expenses[r])):
        if c==0:
            food += monthly_expenses[r][c]
        elif c==1:   
            transport += monthly_expenses[r][c]
        elif c==2:
            utilities += monthly_expenses[r][c]
        if r==0:
            week1 += monthly_expenses[r][c]
        elif r==1:
            week2 += monthly_expenses[r][c]  
        elif r==2:
            week3 += monthly_expenses[r][c]  
        elif r==3:
            week4 += monthly_expenses[r][c]

        

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:',food + transport + utilities)