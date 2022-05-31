def waterArea(heights):
    if len(heights) < 1 or not any(heights):
        return 0

    maximum = max(heights)
    max_Idx = heights.index(maximum)
    i = j = max_Idx
    water_area_left = 0
    water_area_right = 0
    left_array = heights[:j]
    right_array = heights[j+1:]
    return helper(0, i, maximum, water_area_left, left_array) + helper(j+1, len(heights), maximum, water_area_right, right_array)


def helper(start, end, maximum, water_area, array):
    if len(array) < 1:
        return water_area
    current_max = max(array)
    current_max_Idx = elements_between = array.index(current_max)
    nonZero = [x for x in array if x > 0]
    area = current_max * elements_between - sum(nonZero) + current_max
    water_area += area
    if current_max_Idx > 0:
        helper(0, current_max_Idx, current_max,
               water_area, array[0:current_max_Idx])
    return water_area


def waterArea2(heights):
    if len(heights) < 2:
        return 0

    water_trapped = [0 for _ in heights]
    for i in range(1, len(heights) - 1):
        leftPillar = max(heights[j] for j in range(0, i))
        rightPillar = max(heights[j] for j in range(i, len(heights)))

        if leftPillar == 0 or rightPillar == 0:
            continue

        temp = min(leftPillar, rightPillar) - heights[i]
        if temp > 0:
            water_trapped[i] = temp

    return sum(water_trapped)


if __name__ == '__main__':
    heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    print(waterArea2(heights))
