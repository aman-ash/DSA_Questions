def quick_sort(array):
    size = len(array)
    if size <= 1:
        return array
    pivot = array.pop()

    items_greater = []
    items_lower = []

    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    final = quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
    return final


if __name__ == '__main__':
    tests = [
        [78, 98, 54, 123, 72, 256],
        [10, 9, 8, 7, 6, 5],
        [1, 2],
        []
    ]
    for test in tests:
        print(quick_sort(test))
