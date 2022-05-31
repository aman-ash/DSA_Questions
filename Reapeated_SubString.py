def solution(A, B):
    A_dict = {}
    B_dict = {}
    for s in A:
        if s not in A_dict:
            A_dict[s] = 1
        else:
            A_dict[s] += 1
    for s in B:
        if s not in B_dict:
            B_dict[s] = 1
        else:
            B_dict[s] += 1
    for key, values in B_dict.items():
        if key not in A_dict:
            return -1


def sort012(arr):
    for i in range(1, 3):
        for j in range(len(arr)):
            if arr[j] == i:
                tmp = arr.pop(j)
                arr.append(tmp)

    return arr


if __name__ == "__main__":
    arr = [0, 2, 2, 1, 0]
    print(sort012(arr))
