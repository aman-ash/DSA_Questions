def solution(n, houses):
    walk = 0
    home = [1 for _ in range(n)]
    i = 0

    while i < n:
        if houses[i] == str(home[i]):
            i += 1
            continue
        j = k = i
        inLeft = 0
        inRight = 0
        while j > 0:
            if houses[j - 1] == str(home[j]):
                inLeft += 1
                break
            inLeft += 1
            j -= 1

        while k < n - 1:
            if houses[k + 1] == str(home[k]):
                inRight += 1
                break
            inRight += 1
            k += 1

        walk += min(inLeft, inRight)
        i += 1
    return walk


def fun(n, houses):
    walks = 0
    bins = []
    for i in range(len(houses)):
        if houses[i] == str(1):
            bins.append(i)

    for i in range(n):
        if i in bins:
            continue
        mini = float("inf")
        for b in bins:
            current = abs(b - i)
            if current < mini:
                mini = current
        walks += mini

    return walks


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        n = int(input())
        houses = str(input())
        print('Case #%d: %s' % (case+1, fun(n, houses)))
