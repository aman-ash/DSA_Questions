def func(words, k):
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    frequency_list = [[key, value] for key, value in frequency.items()]
    frequency_list = sorted(frequency_list, key=lambda x: x[1])
    return [frequency_list[x][0] for x in range(-1, -1-k, -1)]


if __name__ == '__main__':
    words = ['i', 'i', 'i', 'am', 'am', 'aman', 'aman', 'aman']
    result = func(words, 2)
    print(result)
