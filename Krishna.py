def Solution(string):
    answer = list(string)
    i = 0
    j = len(string) - 1

    while i < j:

        if string[i] == '?' and string[j] == '?':
            answer[i], answer[j] = 'a', 'a'
            i += 1
            j -= 1
            continue

        if string[i] != string[j]:

            if string[i] != '?' and string[j] != '?':
                return "NO"

            if string[i] == '?':
                answer[i] = answer[j]

            else:
                answer[j] = answer[i]

        i += 1
        j -= 1

    return "".join(answer)


if __name__ == "__main__":
    string = '?ab??a'
    a = "bab??a"
    b = '?a?'
    print(Solution(a))
    print(Solution(b))
