class Solution:
    def lsc(self, array):
        lengthDic = {}
        maxLength = max(len(x) for x in array)
        self.createDic(maxLength, array, lengthDic)

        sequences = []
        key = maxLength
        for x in lengthDic[key]:
            nextKey = key - 1

        return lengthDic

    def createDic(self, i, array, dic):
        for j in reversed(range(i+1)):
            dic[j] = []

        for x in array:
            dic[len(x)].append(x)


def main():
    T = int(input())
    for _ in range(T):
        array = list(map(str, input().strip().split()))
        ob = Solution()
        result = ob.lsc(array)
        print(result)


if __name__ == "__main__":
    main()
