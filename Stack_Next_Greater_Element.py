def nextGreaterElement(array):
    ans = [-1 for _ in array]
    if len(array) < 2:
        return [-1]

    for i in range(len(array)):
        current = array[i]
        j = i
        while True:
            if j == len(array):
                j = 0

            if array[j] > array[i]:
                ans[i] = array[j]
                break
            j += 1
            if j == i:
                break
    return ans


if __name__ == '__main__':
    array = {

        1: [],
        2: [-8, -1, -1, -2, -4, -5, -6, 0, -9, -91, -2, 8],
        3: [1, 2, 3, 4, 1, 2, 3, 4, -8, -7, 6, 2, 17, 2, -8, 9, 0, 2],
        4: [2, 6, 7, 2, 2, 2],
        5: [-9, 0, -5, 1, 3, -2, 18, 2, 5, 18],
        7: [12],
        8: [1, 1, 1, 1, 1, 1, 1, 1],
        9: [5, 6, 1, 2, 3, 4],
        10: [7, 6, 5, 4, 3, 2, 1],
        11: [5, 6, 1, 3, 1, -2, -1, 3, 4, 5],
        12:  [1, 0, 1, 0, 1, 0, 1],
        13: [6, 4, 5, 7, 2, 1, 3],
        14: [0, 1, 2, 3, 4]

    }
    for keys, values in array.items():
        print(nextGreaterElement(values))
    print(nextGreaterElement(array[6]))
