def find_min(array):
    min = 99999999999999
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min


def selection_sort(array):
    size = len(array)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]


def findMedian(arr):
    medians = [0 for i in range(len(arr))]
    medians[0] = array[0]
    for i in range(1, len(arr)):
        temp = array[:i+1]
        temp.sort()
        if i % 2 == 0:
            Idx = i // 2
            medians[i] = temp[Idx]
        else:
            Idx1 = i // 2
            Idx2 = Idx1 + 1
            medians[i] = (temp[Idx1] + temp[Idx2]) // 2
    return ' '.join(str(x) for x in medians)


if __name__ == '__main__':
    array = list(map(int, input().split()))
    print(findMedian(array))
