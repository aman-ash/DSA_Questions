def find_sum(arr, k):
    sumDict = {0: 1}
    currentSum = 0
    count = 0

    for a in arr:
        currentSum += a

        if currentSum - k in sumDict:
            count += sumDict[currentSum - k]

        if currentSum in sumDict:
            sumDict[currentSum] += 1

        else:
            sumDict[currentSum] = 1

    return count


if __name__ == '__main__':
    result = find_sum([3, 4, 7, 2, -3, 1, 4, 2, 1], 7)
    print(result)
