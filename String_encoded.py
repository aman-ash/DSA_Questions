def groupAnagrams(words):
    anagram = {}
    for i in range(len(words)):
        current = words[i]
        for j in range(i + 1, len(words)):
            anagrams(current, words[j], anagram)
    return helper(anagram)


def helper(anagram):
    answer = []
    i = 0
    for key, value in anagram.items():
        answer.append([key])
        for v in value:
            answer[i].append(v)
        i += 1
    return answer


def anagrams(str1, str2, dic):
    if len(str1) != len(str2):
        return
    str1_list = list(str1)
    str2_list = list(str2)
    for element in str1_list:
        if element in str2_list:
            str2_list.remove(element)
    if len(str2_list) != 0:
        return
    if str1 in dic:
        dic[str1].append(str2)
    else:
        dic[str1] = [str2]


if __name__ == '__main__':
    string = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(string))
