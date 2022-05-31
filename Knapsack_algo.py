def knapsackProblem(items, capacity):
    new = []
    items = sorted(items, key=lambda x: x[0])
    for i in range(len(items)):
        new.append(items[i][1])
    return new


def subsetsum(array, num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:], (num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:], num)


if __name__ == '__main__':
    test = {
        "capacity": 10,
        "items": [
            [1, 2],
            [4, 3],
            [5, 6],
            [6, 7]
        ]
    }
    cap = test["capacity"]
    items = test["items"]
    print(knapsackProblem(items, cap))
