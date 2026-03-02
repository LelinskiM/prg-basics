class c:
    def __init__ (self, sec):
        self.sec = sec

    def m1(self,s,n):
        self.sec[s] = n
    
    def m2(self,s):
        sum = 0
        for i in s:
            if i in self.sec:
                sum += self.sec[i]
        return sum

Obj = c({"A":120,"D":150,"G":90,"K":110})
Obj.m1("G",130)
print(Obj.m2("GD")) #returns 280
print(Obj.m2("KEJ")) #returns 110 