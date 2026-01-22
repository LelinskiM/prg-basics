def f(n):
    while n>1:
        return n + f(n-1)
    return 1
    
print(f(5))
# Output: 15
print(f(10))
# Output: 55