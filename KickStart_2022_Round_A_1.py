from collections import defaultdict
import bisect


class Solution:
    def func(self, X, Y):
        lcs = self.helper(X, Y)
        return len(Y) - len(X) if lcs else "IMPOSSIBLE"

    def LCS(self, text1, text2):
        arr = []
        d = defaultdict(list)
        for i, char in enumerate(text2):
            d[char].append(i)
        for char in text1:
            if char in d:
                for i in reversed(d[char]):
                    ins = bisect.bisect_left(arr, i)
                    if ins == len(arr):
                        arr.append(i)
                    else:
                        arr[ins] = i
        return len(arr)

    def helper(self, X, Y):
        dx = {}
        for i in X:
            if i in dx:
                dx[i] += 1
            else:
                dx[i] = 1

        for i in Y:
            if i in dx:
                if dx[i] == 0:
                    continue
                dx[i] -= 1

        return not any(list(dx.values()))


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        I = input()
        P = input()
        print('Case #%d: %s' % (case+1, ob.func(I, P)))


if __name__ == '__main__':
    main()
