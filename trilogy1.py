class Solution:

    def func(self, array):
        if len(array) < 2:
            return True
        return self.helper(array)

    def helper(self, array):
        for i in range(0, len(array) - 1):
            if array[i] < array[i + 1]:
                continue
            if not self.check(str(array[i]), array[i + 1]):
                return False

        return True

    def check(self, first, second):
        for i in range(len(first)):
            for j in range(i, len(first)):
                temp = list(first)
                t = temp[i]
                temp[i] = temp[j]
                temp[j] = t

                if int("".join(temp)) < second:
                    return True
        return False


def main():
    ob = Solution()
    T = int(input())
    for _ in range(T):
        array = list(map(int, input().strip().split()))
        result = ob.func(array)
        print(result)


if __name__ == '__main__':
    main()
