def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
            elements[j+1] = anchor

    return elements


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    print(insertion_sort(elements))
