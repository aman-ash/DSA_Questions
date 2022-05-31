class Solution:
    def func(self, phoneNumber):
        keypad = {'0': ['0'], '1': ['1'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        answer = []


def main():
    pn = str(input())
    ob = Solution()
    result = ob.func(pn)
    print(result)


if __name__ == "__main__":
    main()
