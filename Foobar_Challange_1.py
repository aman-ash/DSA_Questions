def solution(s):

    length_of_str = len(s)

    for i in range(1, length_of_str+1):

        cmp_str = s[:i]

        count = s.count(cmp_str)
        if i > length_of_str // 2:
            return 1

        if count*i == length_of_str:
            return count


if __name__ == '__main__':
    str2 = 'abcdefg'
    str1 = 'abcabcabc'
    print(solution(str2))
    print(solution(str1))
