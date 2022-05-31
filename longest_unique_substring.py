def solution(string):
    sets = {}
    max_length = 0
    start_Idx = 0
    for i in range(len(string)):
        current = string[i]
        if current in sets:
            start_Idx = max(start_Idx, sets[current]+1)
        max_length = max(max_length, i - start_Idx + 1)
        sets[current] = i
    return max_length


if __name__ == '__main__':
    string = 'amanamanklopi'
    print(solution(string))
