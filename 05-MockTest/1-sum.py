###
# Calculates the sum of numbers from min_value to max_value
#
total = 0
min_value = 1
max_value = 5
number = min_value

while number <= max_value:
    total = total + number
    number = number + 1

print(f'The sum of the numbers from {min_value} to {max_value} is {total}')