class c:
    def __init__ (self, sectors):
        self.sectors = sectors

    def m1(self,s,n):
        self.sectors[s] = n

    def m2(self,s):
        count = 0
        for sectors in s:
            if sectors in self.sectors:
                count += self.sectors[sectors]
        return count
    
Obj = c({"A":120,"D":150,"G":90,"K":110})
Obj.m1("G",130)
print(Obj.m2("GD")) #returns 280
print(Obj.m2("KEJ")) #returns 110    