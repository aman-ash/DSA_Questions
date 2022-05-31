class Solution:
    def kthGrammar(self, n, k):

        def buildword():
            new = ''
            for w in dp[-1]:
                new += '0' if w == '1' else '1'
            return new

        dp = ["0", "01"]
        if n < 3:
            return self.basecase(n, k)

        for i in range(3, n+1):
            word = dp[-1] + buildword()
            dp.append(word)

        print(dp)
        return dp[-1][k-1]

    def basecase(self, n, k):
        if n < 2:
            return '0'

        return '0' if k == 1 else '1'


if __name__ == '__main__':
    ob = Solution()
    print(ob.kthGrammar(2, 2))
    print(ob.kthGrammar(3, 2))
    print(ob.kthGrammar(5, 6))
