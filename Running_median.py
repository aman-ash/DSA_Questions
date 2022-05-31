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
    print(' '.join(str(x) for x in medians))


if __name__ == '__main__':
    array = list(map(int, input().split()))
    print(findMedian(array))
