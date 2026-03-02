class c:
    def __init__(self,name,age,uni,course,year):
        self.name = name
        self.age = age
        self.uni = uni
        self.course = course
        self.year = year
    def __str__(self):
        out = f'{self.name}{self.age}{self.uni}{self.course[0]}'
        if self.age < 18:
            return out.lower()
        else: return out.upper()

def main():
    print(c("marcel",20,"UEK","Computer Science",1))
    print(c("agnieszka",23,"UJT","Mathematics",3))
    print(c("tomek",17,"UJ","Physics",2))

if __name__ == "__main__":
    main()