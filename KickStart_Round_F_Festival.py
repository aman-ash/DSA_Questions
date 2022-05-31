def fun(D, N, K, Atractions):
    K = int(K)
    happiness = []
    Sdays = [Atractions[i][1] for i in range(int(N))]
    Edays = [Atractions[i][2] for i in range(int(N))]

    for i in range(1, int(D)+1):
        temp = []
        for d in range(len(Edays)):
            if i >= Sdays[d] and i <= Edays[d]:
                temp.append(Atractions[d][0])

        if not len(temp):
            continue

        cur = 0
        if len(temp) < K + 1:
            cur = sum(temp)
        else:
            temp.sort(reverse=True)
            k = 0
            for t in temp:
                cur += t
                k += 1
                if k == K:
                    break

        happiness.append(cur)
    return max(happiness)


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        D, N, K = input().split()
        Atractions = [list(map(int, input().split()))
                      for i in range(int(N))]
        print('Case #%d: %s' % (case+1, fun(D, N, K, Atractions)))
