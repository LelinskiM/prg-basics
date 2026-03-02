class c:
    def __init__ (self, points):
        self.points = points
    def m(self, n):
        count = 0
        for x,y in self.points:
            if x>0 and y>0:
                count += 1
        return count >= n

ob = (c([[2,3],[1,8],[-6,4],[3,-7]]))
print(ob.m(2))
print(ob.m(3))