class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(p):
            if s[i] == p[j]:
                i += 1
                j += 1

            else:
                if p[j] == '.':
                    i += 1
                    j += 1

                elif p[j] == '*':
                    return True

                else:
                    return False

            return False if len(s) < len(p) or i != len(s) else True


if __name__ == '__main__':
    ob = Solution()
    result = ob.isMatch('aa', 'a*')
    print(result)
