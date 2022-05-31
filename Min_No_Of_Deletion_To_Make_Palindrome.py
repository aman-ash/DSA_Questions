class Solution:

    def func(self, string, longest=''):
        if self.isPalindrome(string):
            return string

        for i in range(len(string) - 1):
            newString = string[:i] + string[i+1:]
            newLongest = self.func(newString, longest)
            if len(newLongest) > len(longest):
                longest = newLongest

        return longest

    def isPalindrome(self, str1):
        if len(str1) < 2:
            return True
        i, j = 0, len(str1) - 1
        while i < j:
            if str1[i] != str1[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    string = 'agbcba'
    s1 = 'abacd'
    ob = Solution()
    print(ob.func(s1))
