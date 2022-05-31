def globMatching(fileName, pattern):
    i = j = 0
    while i < len(fileName) and j < len(pattern):
        if pattern[j] == '*':
            if i == len(fileName) - 1:
                return True
            Idx = j + 1
            while fileName[i] != pattern[Idx]:
                i += 1

        elif pattern[j] == '?':
            i += 1

        else:
            if fileName[i] != pattern[j]:
                return False
            i += 1
            j += 1

    return True


if __name__ == '__main':
    fileName = 'abcdefg'
    pattern = 'a*e?g'
    print(globMatching(fileName, pattern))
