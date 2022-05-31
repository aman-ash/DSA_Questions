def shiftedBinarySearch(array, target):
    sortarray(array)
    return array
    return binarySearch(array, target, 0, len(array) - 1)


def sortarray(array):
    Idx = array.index(min(array))
    for i in range(Idx):
        tmp = array.pop(i)
        array.append(tmp)


def binarySearch(array, target, left=0, right=0):
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        current = array[mid]

        if current > target:
            right = mid - 1
        elif current < target:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    target = 33
    print(shiftedBinarySearch(array, target))
