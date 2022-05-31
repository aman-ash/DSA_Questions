def magicIndex(a, n):
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if mid > a[mid]:
            l = mid + 1
        elif mid < a[mid]:
            r = mid
        else:
            return mid
    return -1


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(magicIndex(a, n))
