def longestIncreasingSubsequence(array):
    if len(array) < 2:
        return array
    longest = []

    for i in range(len(array) - 1):
        current = array[i]
        longestTillNow = [current]
        for j in range(i + 1, len(array)):

            if array[j] > current:
                longestTillNow.append(array[j])
                current = array[j]
            if array[j] < current:
                if isValid(longestTillNow, array[j]):
                    longestTillNow[-1] = array[j]
                    current = array[j]

        if len(longestTillNow) > len(longest):
            longest = longestTillNow

    return longest


def isValid(arr, num):
    for i in range(len(arr) - 1):
        if arr[i] > num:
            return False
    return True


if __name__ == '__main__':
    print(longestIncreasingSubsequence([1,  11, 13, 2, 3, 12, 13, 4, 5, 6]))
