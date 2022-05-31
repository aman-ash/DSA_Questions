def globMatching(fileName, pattern):
    i = j = count = 0
    for p in pattern:
        if p == '*':
            count += 1
    if count == len(pattern):
        return True

    if not any(fileName):
        for p in pattern:
            if p != '*':
                return False
        return True

    if not any(pattern):
        return fileName == pattern

    while i < len(fileName) and j < len(pattern):
        if pattern[j] == '*':
            if j == len(pattern) - 1:
                return True
            Idx = j
            while pattern[Idx] == '*':
                Idx = Idx + 1
            while fileName[i] != pattern[Idx]:
                if i == len(fileName) - 1:
                    return False
                i += 1
            j += 1

        elif pattern[j] == '?':
            i += 1

        else:
            if fileName[i] != pattern[j]:
                return False
            i += 1
            j += 1

    return True


def ans(A, B):
    j = 0
    left = 0
    answer = False
    for i in range(len(B)):
        anchor = B[i]

        for num in range(left, len(A)):
            if anchor == A[num]:
                left = num
                answer = True
            else:
                answer = False
    return answer


if __name__ == "__main__":
    fileName = 'abcdefg'
    pattern = '***g'
    print(globMatching(fileName, pattern))
