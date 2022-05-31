def solution(n, a):
    count = 0
    for i in range(0, n-2):
        if a[i] != a[i + 2]:
            count += 1

        s = set(a)
        if len(s) == 1:
            if len(a) == 3:
                return 1
            else:
                return 2
    return count


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(solution(n, a))
