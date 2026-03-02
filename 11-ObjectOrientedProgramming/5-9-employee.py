class c:
    def __init__(self,name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    def __str__(self):
        out = f'{self.surname}{self.name[0]}{self.seniority}'
        if self.age >= 18:
            return out.upper()
        else:  
            return out.lower() 

print(c("Anna","May",17,7))
print(c("George","Brown",21,4))