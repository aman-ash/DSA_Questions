def fun(n, updates):
    ans = [0 for _ in range(n)]
    for update in updates:
        for i in range(update[0], update[1]+1):
            ans[i] += update[2]

    return ans


if __name__ == '__main__':
    n = int(input())
    q = int(input())
    updates = [[int(input()) for _ in range(3)] for i in range(q)]
    print(fun(n, updates))
