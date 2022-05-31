def get_shortest_unique_substring(arr, st):
    di = dict([key, 0] for key in arr)
    i, j = 0, 0
    subString = st[:]
    found = False

    while i < len(st) and j < len(st):
        if st[j] in di:
            di[st[j]] += 1

        if all(di.values()):
            found = True
            cur = st[i:j + 1]

            if len(cur) < len(subString):
                subString = cur

            a = list(di.values())
            while a != [1] * len(a):
                if 0 in di.values():
                    break
                if st[i] in di:
                    di[st[i]] -= 1
                i += 1
                a = list(di.values())

        j += 1

    return subString if found else ""


if __name__ == "__main__":
    arr = ["A", "B", "C"]
    st = "ADOBECODEBANCDDD"
    print(get_shortest_unique_substring(arr, st))
