def sunsetViews(buildings, direction):
    if direction == "WEST":
        return helper(buildings, 1, len(buildings), 1)
    return helper(buildings, len(buildings) - 1, -1, -1)


def helper(array, idx, end, ran):
    ans = []
    temp = 0 if idx == 1 else idx
    current = array[0 if idx == 1 else idx]
    ans.append(temp)

    for i in range(idx, end, ran):
        if array[i] > current:
            ans.append(i)
            current = array[i]
    ans.sort()
    return ans


if __name__ == '__main__':
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    print(sunsetViews(buildings, "WEST"))
    print(sunsetViews(buildings, "EAST"))
