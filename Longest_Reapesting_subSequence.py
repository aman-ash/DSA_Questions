def LongestRepeatingSubsequence(str1):
    sub = 0
    dic = {}
    i = 0
    count = 0
    while i < len(str1):
        if str1[i] in dic:
            if count == str1[i]:
                i += 1
                continue
            dic[str1[i]] += 1

        else:
            dic[str1[i]] = 1
            count = str1[i]

        i += 1

    for key, value in dic.items():
        sub = max(sub, value)
    if sub == 1:
        return 0
    return sub


if __name__ == "__main__":
    str1 = 'agcsorvauz'
    print(LongestRepeatingSubsequence(str1))
