def recursive(arr, element, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] > element:
        return recursive(arr, element, left, mid)
    elif arr[mid] < element:
        return recursive(arr, element, mid+1, right)
    else:
        return mid


def itretive(arr, element):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < element:
            left = mid + 1
        elif arr[mid] > element:
            right = mid
        else:
            return mid
    return -1


def main(arr, element):
    print(recursive(arr, element, 0, len(arr) - 1))
    return itretive(arr, element)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    element = 15
    print(main(arr, element))
