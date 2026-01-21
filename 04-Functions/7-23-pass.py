def f(password):

    if len(password) < 6:
        return False
    else:
        count = 0
        x=0
        for i in password:
            x +=1
            y=0
            for j in password:
                y +=1
                if x != y:
                    if i == j:
                        count += 1
            if count > 1:
                return False
    return True

print(f("ax15")) #returns False
print(f("book123")) #returns False
print(f("A2water3")) #returns True
print(f("qwerty")) #returns True
print(f("")) #returns False
            