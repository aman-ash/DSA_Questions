def solution(value):
    for j in range(len(value)):
        letter = value[j]
        count = 1
        for i in range(j, len(value)):
            if i == j:
                continue
            if letter == value[i]:
                count += 1
        if count > (len(value) // 2):
            return "IMPOSSIBLE"
    return anagram(value)


def anagram(word):
    newWord = list(word)
    positions = {}
    for letter in word:
        Idx = newWord.index(letter)
        if letter in positions:
            positions[letter].append(Idx)
        else:
            positions[letter] = [Idx]
        newWord[Idx] = ''
    anagrams = ['' for _ in range(len(word))]
    new_index = {}
    for key, value in positions.items():
        for i in range(len(value)):
            for j in range(len(anagrams)):
                if value[i] != j:
                    if key in new_index:
                        new_index[key].append(j)
                    else:
                        new_index[key] = [j]
                    break
    return new_index


if __name__ == '__main__':
    t = int(input())
    case = 1
    while t > 0:
        value = str(input())
        print("Case #"+str(case) + ": " + str(solution(value)))
        t -= 1
        case += 1
