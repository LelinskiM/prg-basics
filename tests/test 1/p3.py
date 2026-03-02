def f(password):
    count =0
    if len(password) < 6:
        return False
    else:
        for letter in password:
            for letter1 in password:
                if letter == letter1:
                    count+=1
        if count >len(password):
            return False    
        else:
            return True
