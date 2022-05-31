class Solution:
    def func(self, string):
        if len(string) < 3:
            return 0
        i = j = 0
        stringReversed = string[::-1]
        ans = []
        ansReversed = []
        self.findCuts(string, i, j, ans)
        self.findCuts(stringReversed, i, j, ansReversed)
        return len(ans) - 1 if len(ans) < len(ansReversed) else len(ansReversed) - 1

    def findCuts(self, string, i, j, ans):
        if len(string) < 2:
            ans.append(string)
            return ans
        temp = []
        while i < len(string) and j < len(string):
            palindrome = self.checkPalindrome(string[i:j+1])
            if palindrome:
                temp.append(string[i:j+1])
            j += 1
        longest = max(temp)
        ans.append(longest)

        self.findCuts(string[len(longest):], 0, 0, ans)

    def checkPalindrome(self, string):
        if len(string) < 2:
            return True
        start = 0
        end = len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True


def main():
    ob = Solution()
    T = int(input())
    for _ in range(T):
        string = str(input())
        print(ob.func(string))


if __name__ == "__main__":
    main()
