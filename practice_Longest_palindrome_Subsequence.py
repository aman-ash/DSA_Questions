def main(s):
    return lcs(s, s[::-1])


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    memo = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return helper(s1, s2, memo)


def helper(s1, s2, memo):
    n, m = len(s1), len(s2)
    lps = ''
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lps += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if memo[i - 1][j] > memo[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return lps


if __name__ == "__main__":
    s = 'abcedba'
    print(main(s))
