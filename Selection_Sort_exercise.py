def find_min(array):
    min = 99999999999999
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min


def selection_sort(array, key):
    size = len(array)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if key == 'First Name':
                if array[j]['First Name'] < array[min_index]['First Name']:
                    min_index = j
            if key == 'Last Name':
                if array[j]['Last Name'] < array[min_index]['Last Name']:
                    min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]


if __name__ == '__main__':
    elements = [
        {'First Name': 'Aahana', 'Last Name': 'Arora'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'}
    ]
    key = 'Last Name'
    selection_sort(elements, key)
    print(elements)
