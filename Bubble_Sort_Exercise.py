
def bubble_sort(elements):
    size = len(elements)

    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):

            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        if not swapped:
            break


def bubble_sort_dict(elements, key):
    size = len(elements)

    for k in range(size-1):
        swapped = False
        for i in range(size-1-k):
            if key == 'name':
                if elements[i]['name'] > elements[i+1]['name']:
                    temp = elements[i]
                    elements[i] = elements[i+1]
                    elements[i+1] = temp
                    swapped = True

            if key == 'amount':
                if elements[i]['transaction_amount'] > elements[i+1]['transaction_amount']:
                    temp = elements[i]
                    elements[i] = elements[i+1]
                    elements[i+1] = temp
                    swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    array = [7, 8, 4, 1, 2, 3, 4, 5]
    elements = [
        {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    # bubble_sort(elements, 'name')
    bubble_sort_dict(elements, 'amount')
    print(elements)
    bubble_sort_dict(elements, 'amount')
    print(elements)
