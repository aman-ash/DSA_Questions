class Solution:
    def func(self, array):
        permutations = []
        self.helper(0, array, permutations)
        return permutations

    def helper(self, i, array, permutations):
        if i == len(array) - 1:
            permutations.append(array[:])
        else:
            for j in range(i, len(array)):
                self.swap(array, i, j)
                self.helper(i + 1, array, permutations)
                self.swap(array, i, j)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


def main():
    ob = Solution()
    T = int(input())
    for _ in range(T):
        array = list(map(int, input().split()))
        result = ob.func(array)
        print(result)


if __name__ == "__main__":
    main()
