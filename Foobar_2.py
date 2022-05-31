def solution(s):
    salute = 0
    for i in range(len(s)):
        if s[i] == '<' or '>':
            for j in range(i+1, len(s)):
                if s[i] == '>':
                    if s[j] == '<':
                        salute += 1
                else:
                    if s[j] == '>':
                        salute += 1

    return salute


def answer(s):
    # your code herecat
    multiplier = 0
    salute = 0
    for x in range(len(s)):
        if s[x] == '<':
            multiplier += 1

    for x in range(len(s)):
        if s[x] == '>':
            salute += multiplier
        elif s[x] == '<':
            multiplier -= 1

    ans = salute * 2

    return ans


if __name__ == '__main__':
    s = '<<>><'
    s2 = '>----<'
    print(answer(s2))
    print(answer(s))
