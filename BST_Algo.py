def sol(array):
    idx = len(array) // 2
    root = array.pop(idx)
    print(root)
    print(array)


if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    sol(array)
