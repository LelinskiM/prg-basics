###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    x=abs(any_number)
    Digit_sum = sum(int(i) for i in str(x))
    return Digit_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')