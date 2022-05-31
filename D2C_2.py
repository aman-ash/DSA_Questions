# final solution


def solution(array, n):
    count = 0
    i = 1
    while i < n - 1:
        small = min(array[i - 1], array[i], array[i + 1])
        large = max(array[i - 1], array[i], array[i + 1])
        if small != array[i] and large != array[i]:
            count += 1

        i += 1

    return count


if __name__ == '__main__':
    n = int(input())
    array = list(map(str, input().strip().split()))
    print(solution(array, n))
