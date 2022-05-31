memo = {}


class Solution:
    def superEggDrop(self, e, f):
        if e == 1 or f == 1 or f == 0:
            return f

        key = str(e) + '.' + str(f)

        if key in memo:
            return memo[key]

        mn = float("inf")
        for k in range(1, f+1):
            bkey = str(e-1) + '.' + str(k-1)
            notbkey = str(e) + '.' + str(f-k)
            if bkey not in memo:
                memo[bkey] = self.superEggDrop(e-1, k-1)

            if notbkey not in memo:
                memo[notbkey] = self.superEggDrop(e, f-k)

            temp = 1 + max(memo[bkey], memo[notbkey])
            mn = min(mn, temp)

        memo[key] = mn
        return mn


if __name__ == '__main__':
    ob = Solution()
    print(ob.superEggDrop(3, 14))
