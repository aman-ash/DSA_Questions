class Solution:
    def func(self, S):
        return self.helper(S)

    def helper(self, S):
        Done = False
        i = 0
        op = ['01', '12', '23', '34', '45', '56', '67', '78', '89', '90']
        operations = {'01': '2', '12': '3', '23': '4', '34': '5',
                      '45': '6', '56': '7', '67': '8', '78': '9', '89': '0', '90': '1'}

        while i < len(op):
            if op[i] in S:
                Done = True
                k = S.index(op[i])
                j = k + 1

                B = S[:k]
                temp = operations[op[i]]
                A = S[j+1:]

                S = B + temp + A
            else:
                i += 1

        if Done:
            self.helper(S)

        return S


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        n = int(input())
        S = str(input())
        print('Case #%d: %s' % (case+1, ob.func(S)))


if __name__ == '__main__':
    main()
