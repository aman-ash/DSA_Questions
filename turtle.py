
def search(A, l, h, key):
    return helper(A, l, h, key)


def helper(A, l, h, key):
    mid_Idx = (l + h)//2
    if A[mid_Idx] == key:
        return mid_Idx

    elif A[mid_Idx] < key:
        if A[l] < key:
            return helper(A, l,  mid_Idx - 1, key)
        elif A[l] > key:
            return helper(A, mid_Idx+1, h, key)
        else:
            return l

    else:
        if A[l] < key:
            return helper(A, l,  mid_Idx - 1, key)
        elif A[l] > key:
            return helper(A, mid_Idx+1, h, key)
        else:
            return l

    return -1


if __name__ == "__main__":
    A = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    l = 0
    h = len(A) - 1
    key = 10
    key2 = 2
    print(search(A, l, h, key))
