from itertools import permutations


def maximizeExpression(array):
    if len(array) < 4:
        return 0

    ans = float("-inf")
    for a in range(len(array) - 3):
        for b in range(a+1, len(array) - 2):
            for c in range(b+1, len(array) - 1):
                for d in range(c+1, len(array)):
                    if a < b and b < c and c < d:
                        sums = array[a] - array[b] + \
                            array[c] - array[d]
                        ans = max(ans, sums)
    return ans


def func(array):
    ans = float("-inf")
    N = [i for i in range(len(array))]
    perm = permutations(N, 4)
    for i in list(perm):
        if i[0] < i[1] and i[1] < i[2] and i[2] < i[3]:
            sums = array[i[0]] - array[i[1]] + array[i[2]] - array[i[3]]
            ans = max(sums, ans)

    return ans


if __name__ == '__main__':
    array = [3, 6, 1, -3, 2, 7]
    print(func(array))
