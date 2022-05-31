def longestStringChain(strings):
    ans = []
    graph = buildGraph(strings)
    for key, value in graph.items():
        chain = [key]
        ans = helper(key, value, graph, chain, ans)

    ans.sort(key=lambda x: len(x), reverse=True)
    return ans


def helper(key, value, graph, chain, ans):

    for val in value:
        if check(key, val):
            chain.append(val)
            helper(val, graph[val], graph, chain, ans)
        else:
            if len(chain) > len(ans):
                ans = chain

    return ans


def check(a, b):
    if len(a) > len(b) + 1:
        return False
    mapB = {}
    for s in b:
        if s in mapB:
            mapB[s] += 1
        else:
            mapB[s] = 1
    # print(mapB)
    for s in a:
        if s in mapB:
            mapB[s] -= 1
    # print(mapB)
    return not any(list(mapB.values()))


def buildGraph(arr):
    arr.sort(key=lambda x: len(x), reverse=True)
    graph = {}
    for i in range(len(arr) - 1):
        cur = arr[i]
        temp = []
        for j in range(i+1, len(arr)):
            if len(arr[j]) < len(cur) - 1:
                break
            if len(arr[j]) >= len(cur):
                continue
            temp.append(arr[j])
        graph[cur] = temp
    graph[arr[-1]] = []
    return graph

#print(check('abcda', 'abac'))


if __name__ == '__main__':
    arr = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
    print(longestStringChain(arr))
