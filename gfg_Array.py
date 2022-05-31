class Solution:
    def removeDups(self, S):
        new = {}

        for s in S:
            if s not in new:
                new[s] = True

        return "".join(new.keys())


def main():
    S = 'zvvo'
    ob = Solution()
    result = ob.removeDups(S)
    print(result)


if __name__ == '__main__':
    main()
