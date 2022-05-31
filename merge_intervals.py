def merge(intervals):
    if len(intervals) < 2:
        return intervals

    new = [intervals[0]]

    for i in range(1, len(intervals)):
        cur = intervals[i]
        prev = new[- 1]

        if cur[0] <= prev[1]:
            start = min(cur[0], prev[0])
            end = max(cur[1], prev[1])
            new[i - 1] = ([start, end])

        else:
            new.append(intervals[i])

    return new


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
