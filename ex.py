def longestCommonSubsequence(str1, str2):
    j = 0
    Idx = 0
    answer = []
    list1 = []
    list2 = []
    for i in str1:
        list1.append(i)
    for i in str2:
        list2.append(i)
    for i in range(len(list1)):
        j = Idx
        char1 = list1[i]
        while j < len(list2):
            char2 = list2[j]
            if char1 == char2:
                answer.append(char1)
                Idx += 1
                break
            j += 1
    return answer


str1 = "ABCDEFG"
str2 = "APPLES"
str3 = "ZXVVYZW"
str4 = "XKYKZPW"
print(longestCommonSubsequence(str3, str4))
