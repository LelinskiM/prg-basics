class C:
    def __init__(self,count):
        self.count = count
    def m1(self):
        return self.count
    def m2(self):
        self.count+=10
    def m3(self):
        self.count-=10
    def m4(self,n):
        self.count+=n
    def __str__(self):
        return self.count