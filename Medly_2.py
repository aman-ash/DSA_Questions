def func(n):
    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2
        current = 2 ** mid

        if current > n:
            high = mid - 1

        elif current < n:
            low = mid + 1

        else:
            current //= 2
            break

    while current > n:
        current //= 2

    return current


if __name__ == '__main__':
    tests = [100, 50, 2000, 4, 2, 10, 17, 3, 19]
    for test in tests:
        print(func(test))
