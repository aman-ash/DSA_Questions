def solution(S):
    temp = []
    count = 0

    for s in S:
        if s == 'a':
            count += 1

    if count > 0 and count % 3 == 0:
        return 0

    no = count // 3

    occur = 0
    i = 0
    while i < len(S):
        if S[i] == 'a':
            for j in range(i, len(S)):
                if S[j] == 'a':
                    occur += 1

                if occur == no:
                    temp.append('a')
                    occur = 0
                    i = j
                    break

                j += 1
        else:
            temp.append(S[i])
            i += 1

        if occur == no:
            temp.append(s)
            occur = 0

    ans = 0
    for i in range(1, len(temp) - 1):
        if temp[i] == 'a':
            if temp[i - 1] == 'b':
                ans += 1
            if temp[i + 1] == 'b':
                ans += 1

    return ans


if __name__ == "__main__":
    pass
