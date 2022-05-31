def fun(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return fun(left, right)


if __name__ == "__main__":
    # a = [1, 7, 89, 1235]
    # b = [9, 45, 62]
    # print(fun(a, b))
    array = [7, 2, 1, 5, 9, 87, 9, 6, 3, 4, 6, 2]
    print(merge_sort(array))
