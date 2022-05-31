
def bubble_sort(elements):
    size = len(elements)

    for k in range(size-1-1):
        swapped = False
        for i in range(size-1):

            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    element = [24, 6, 11, 7, 89, 12, 789]
    array = [1, 2, 3, 4, 5]
    names = ['jungkook', 'jimin', 'suga', 'v', 'jin', 'rm', 'j-hope']
    name = ['az', 'bc']
    bubble_sort(names)
    bubble_sort(name)
    print(names)
    print(name)
