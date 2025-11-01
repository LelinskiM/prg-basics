N = int(input("Enter a number: "))
count = 0
x = 2

while x <= N:
    is_prime = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime and x > 1:
        print(x)
        count +=  1
    x += 1
    
