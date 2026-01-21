def f(n):
    result = 0
    current_Num = 0
    sign = 1  # 1 for positive, -1 for negative

    for char in n:
        if char.isdigit():
            current_Num = int(char)
            result += sign * current_Num
        elif char == '+':
            sign = 1
        elif char == '-':   
            sign = -1
    return result

print(f("2+3")) #returns 5
print(f("3+8+1")) #returns 12
print(f("2+3-4+5-0")) #returns 6