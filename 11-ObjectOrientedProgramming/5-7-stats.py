class stats:
    def __init__ (self):
        self.num = []
    
    def add_num(self, num):
        self.num.append(num)
    
    def show_nums(self):
        print("numbers: ", end=" ")
        for num in self.num:
            print(num, end=" ")
        print()

    def get_max(self):
        max = self.num[0]
        for num in self.num:
            if num > max:
                max = num
        return max

    def get_min(self):
        min = self.num[0]
        for num in self.num:
            if num < min:
                min = num
        return min
    
    def mean(self):
        sum = 0
        for num in self.num:
            sum += num
            return sum / len(self.num)
    
    def median(self):
        sorted_nums = sorted(self.num)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            return sorted_nums[mid]
        
    def show(self):
        self.show_nums()
        print("max: ", self.get_max())
        print("min: ", self.get_min())
        print("mean: ", self.mean())
        print("median: ", self.median())
        
def main():
    s = stats()
    data = [12, 37, 6, 9, 17]

    for num in data:
        s.add_num(num)

    s.show()

if __name__ == "__main__":
    main()