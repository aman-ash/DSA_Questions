# final solution


def solution(array, n):
    answer = []
    if n < 2:
        return array

    for i in range(n):
        rotate = []
        answer.append(array[i])
        for j in reversed(range(i+1)):
            rotate.append(answer[j])
        answer = rotate
    return " ".join(rotate)


if __name__ == '__main__':
    n = int(input())
    array = list(map(str, input().strip().split()))
    print(solution(array, n))
