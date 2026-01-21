def f(n):
    if len(n)<= 1:
        return str(n)
    else:
        return f(n[:-1]) + '-' + str(n[-1])

print(f("Univesity")) # returns "U-n-i-v-e-r-s-i-t-y"
print(f("UE")) # returns "U-E"
print(f("x")) # returns "x"
print(f("")) # returns ""