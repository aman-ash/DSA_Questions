def prep_bubble_sort(array):
    size = len(array)
    swapped = False
    for i in range(size-1):
        if array[i] > array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp

    return array


if __name__ == '__main__':
    array = [11, 89, 789, 25, 1]
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, ]
    print(prep_bubble_sort(array))
