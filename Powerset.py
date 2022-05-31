class Solution:
    def func(self, array):
        subset = [[]]
        for element in array:
            for i in range(len(subset)):
                cur = subset[i]
                subset.append(cur + [element])
        return subset


def main():
    ob = Solution()
    T = int(input())
    for _ in range(T):
        array = list(map(int, input().strip().split()))
        result = ob.func(array)
        print(result)


if __name__ == "__main__":
    main()
