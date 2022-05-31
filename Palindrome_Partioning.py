def main(string):
    dp = [[-1 for _ in range(len(string))] for _ in range(len(string))]
    return solve(string, 0, len(string) - 1, dp)


def solve(s, i, j, dp):
    if i >= j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if isPlaindrome(s[i:j+1]):
        return 0

    ans = float("inf")
    for k in range(i, j):
        l = dp[i][k] if dp[i][k] != -1 else solve(s, i, k, dp)
        r = dp[k+1][j] if dp[k+1][j] != -1 else solve(s, k+1, j, dp)
        temp = l + 1 + r
        ans = min(ans, temp)
    return ans


def isPlaindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.helper(string, 0, n-1, memo)

    def helper(self, s, i, j, memo):
        if i >= j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        if self.isPalindrome(s, i, j):
            memo[i][j] = 0
            return memo[i][j]

        ans = float("inf")
        for k in range(i, j):
            if memo[i][k] == -1:
                memo[i][k] = self.helper(s, i, k, memo)
            l = memo[i][k]

            if memo[k+1][j] == -1:
                memo[k+1][j] = self.helper(s, k+1, j, memo)
            r = memo[k+1][j]

            temp = l + 1 + r
            ans = min(ans, temp)

        memo[i][j] = ans
        return memo[i][j]

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    ob = Solution()
    s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
    print(ob.palindromicPartition(s))
