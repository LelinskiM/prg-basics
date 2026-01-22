def f(x,n):
    while n>1:
        return x*f(x,n-1)
    return x

print(f(2,5))  # Should print 32
print(f(3,4))  # Should print 81
print(f(5,2))  # Should print 25