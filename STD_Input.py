def countStepsToOne(n):
    steps = [0 for _ in range(n + 1)]
    steps[1] = 0
    steps[2] = 1
    steps[3] = 1
    for i in range(4, n+1):
        count = 0
        Idx = i
        while i != 1:
            while i % 3 == 0:
                i = i // 3
                count += 1
            while i % 2 == 0:
                i = i // 2
                count += 1
            if i != 1:
                i -= 1
                count += 1
        steps[Idx] = count
    return steps[n]


if __name__ == '__main__':
    n = 5
    print(countStepsToOne(n))
