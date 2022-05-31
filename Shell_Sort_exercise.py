def check_duplicate(array):
    not_duplicate = []
    for element in array:
        if element not in not_duplicate:
            not_duplicate.append(element)
    return not_duplicate


def shell_sort(array):
    size = len(array)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = array[i]
            j = i
            while j >= gap and array[j - gap] > anchor:
                array[j] = array[j-gap]
                j -= gap
            array[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9, 32]
    shell_sort(elements)
    print(elements)
    print(check_duplicate(elements))
