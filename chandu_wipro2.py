def main(p, q):
    ans = []
    for i in range(len(p)):
        ans.append(p[i])
        ans.append(q[i])
    return ans


n = int(input())
p = list(input().split())
m = int(input())
q = list(map(int, input().split()))
print(*main(p, q))
