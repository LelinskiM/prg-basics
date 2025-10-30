###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >=7:
    quarter = 3
elif month >=4:
    quarter = 2
elif month>=1:
    quarter=1
else:
    print("error")

print(f'Month {month} is in quarter {quarter}')