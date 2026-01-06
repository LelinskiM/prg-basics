def f(n1,n2,op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    elif op == "%":
        return n1 % n2
    elif op == "**":
        return n1 ** n2
    else:
        return "Invalid operation"

print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))