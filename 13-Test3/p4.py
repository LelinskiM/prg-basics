class C:
    def __init__(self,Fname,age):
        self.Fname = Fname
        self.age = age
    def __str__(self):
        out = f'{self.Fname[0]}-{self.age}'
        if self.age>=18:
            return out.upper()
        else:
            return out.lower()

