###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
x=N
sum_even = 0

# Calculate the sum of even numbers
while N+1 > 0:
#for i in range(1, N + 1):
    if N % 2 == 0:
        sum_even += N
    N-=1

print(f"The sum of even numbers from 1 to {x} is: {sum_even}")