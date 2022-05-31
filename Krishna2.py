def solution(blocks):
    answer = []

    if not blocks:
        return -1

    if len(blocks) < 2:
        return 1

    for i in range(len(blocks)):
        j = i

        while i > 0:
            if blocks[i] <= blocks[i - 1]:
                i -= 1
            else:
                break

        while j < len(blocks) - 1:
            if blocks[j] <= blocks[j + 1]:
                j += 1
            else:
                break

        temp = i - j + 1 if i > j else j - i + 1
        answer.append(temp)

    return max(answer)


if __name__ == "__main__":
    blocks = []
    a = [1, 5, 5, 2, 6]
    b = [1]

    print(solution(a))
    print(solution(blocks))
    print(solution(b))
