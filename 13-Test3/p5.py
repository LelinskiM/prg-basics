class C:
    def __init__(self,sectors):
        self.sectors=sectors
    def m1(self,s,n):
        self.sectors[s]=n
    def m2(self,s):
        total = 0
        leng = 0
        for sector in self.sectors:
            if sector in s:
                leng +=1
                total += self.sectors[sector]
        return total/leng        