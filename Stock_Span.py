class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price):
        Idx = self.count
        self.count += 1
        return self.getAns(price, Idx)

    def getAns(self, price, Idx):
        if self.stackIsEmpty():
            self.stack.append([price, Idx])
            return Idx + 1

        while len(self.stack):
            if self.stack[-1][0] > price:
                ans = Idx - self.stack[-1][1]
                self.stack.append([price, Idx])
                return ans
            else:
                self.stack.pop()
        self.stack.append([price, Idx])
        return Idx + 1

    def stackIsEmpty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    ob = StockSpanner()
    arr = [100, 80, 60, 70, 60, 75, 85]
    aa = [29, 91, 62, 76, 51]
    for i in range(len(aa)):
        print(ob.next(aa[i]))
