

def race(s, queries):
    ans = []
    for i in range(len(queries)):
        st, e = queries[i][0] - 1, queries[i][1]
        temp = {}
        for j in range(st, e):
            if s[j] in temp:
                temp[s[j]] += 1
            else:
                temp[s[j]] = 1
        ans.append(max(list(temp.values())))

    return ans


memo = {}


def main(boxes):
    ans = [0]
    solve(boxes, len(boxes), ans)
    return ans[0]


def solve(boxes, n, a):
    if n == 1:
        return boxes[n - 1]

    key = str(boxes)

    if key in memo:
        return memo[key]

    cur = sum([boxes[i] for i in range(0, len(boxes), 2)]) - \
        sum([boxes[i] for i in range(1, len(boxes), 2)])

    for i in range(n):
        ans = max(cur, solve(boxes[:i] + boxes[i+1:], n-1, a))
    a[0] = max(a[0], ans)

    memo[key] = ans
    return ans


def solveTopDownDP(boxes):
    ans = boxes[0]
    for i in range(1, len(boxes)):
        cur = ans + boxes[i] - boxes[i-1]
        ans = max(ans, cur)
    return ans


if __name__ == '__main__':
    boxes = [[5, 6, 2], [9, 5, 2, 9, 4], [
        8, 6, 2, 7, 7, 2, 7], [1, 2, 3, 4, 5, 6], [6, 1,  2, 8]]
    for box in boxes:
        print(main(box))
        print(solveTopDownDP(box))
