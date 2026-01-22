def f(n):
    while n>1:
        return n * f(n-1)
    return 1

print(f(5))  # Output: 120