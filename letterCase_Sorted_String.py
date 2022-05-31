class Solution:

    def caseSort(self, s):
        lowLetters = ['' for _ in range(len(s))]
        upLetters = ['' for _ in range(len(s))]
        lowIdx = []
        upIdx = []

        ans = ['' for _ in range(len(s))]

        for i in range(len(s)):
            if s[i].isupper():
                upIdx.append(i)
                upLetters[i] = (s[i])

            else:
                lowIdx.append(i)
                lowLetters[i] = (s[i])

        if lowLetters:
            lowLetters.sort()
        if upLetters:
            upLetters.sort()

        for i in lowIdx:
            ans[i] = lowLetters[i]

        for i in upIdx:
            ans[i] = upLetters[i]

        return ''.join(ans)


if __name__ == '__main__':
    s = 'defRTSersUXI'
    ob = Solution()
    result = ob.caseSort(s)
    print(result)
