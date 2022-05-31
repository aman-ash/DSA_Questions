from Decorater import time_it


def linear_search(numbers_list, number_to_find):
    no = []
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            no.append(index)
            return index
    return -1


def Binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        indexing = []
        if mid_number == number_to_find:
            return mid_index

        elif mid_number > number_to_find:
            right_index = mid_index - 1

        else:
            left_index = mid_index + 1

    return -1


def Binary_search_Recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]
    indexing = []

    if mid_number == number_to_find:
        return mid_index

    elif mid_number > number_to_find:
        right_index = mid_index - 1

    else:
        left_index = mid_index + 1

    return Binary_search_Recursive(numbers_list, number_to_find,
                                   left_index, right_index)


def find_all_occurances(numbers, number_to_find):
    index = Binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    numbers_list = [6, 6, 7, 11, 24, 48, 59, 78, 85, 711]
    numbers = [5 for i in range(1, 100)]

    # print(linear_search(numbers_list, number_to_find))
    # index = Binary_search(numbers_list, 6)
    # print(f"Element is at {index} index.")

    print(find_all_occurances(numbers, 5))
