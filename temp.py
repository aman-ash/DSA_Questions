def func(arr, n):
    n_sum = 0
    s = set()

    for i in range(n):
        n_sum += arr[i]

        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)

    return False


def main():
    for i in range(int(input())):

        arr = list(map(int, input().strip().split()))
        result = func(arr, len(arr))
        print(result)


if __name__ == '__main__':
    main()
