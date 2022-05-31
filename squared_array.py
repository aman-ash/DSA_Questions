def sortedSquaredArray(array):
    answer = []
    for i in array:
        answer.append(i*i)

    return answer
if __name__ == '__main__':
    array = [0,5,5,10,10]
    print(sortedSquaredArray(array))