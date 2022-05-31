def merge_two_sorted_lists(a, b, array, key):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if key == 'name':
            if a[i]['name'] < b[j]['name']:
                array[k] = a[i]
                i += 1
            else:
                array[k] = b[j]
                j += 1
            k += 1
        if key == 'time_hours':
            if a[i]['time_hours'] < b[j]['time_hours']:
                array[k] = a[i]
                i += 1
            else:
                array[k] = b[j]
                j += 1
            k += 1

    while i < len_a:
        array[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        array[k] = b[j]
        j += 1
        k += 1


def merge_sort(array, key):
    if len(array) <= 1:
        return

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left, key)
    merge_sort(right, key)

    merge_two_sorted_lists(left, right, array, key)


if __name__ == '__main__':
    elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
    key = 'name'
    merge_sort(elements, key)
    print(elements)
