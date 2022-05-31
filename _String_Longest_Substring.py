def longestSubstringWithoutDuplication(string):
    if len(string) < 2:
        return string
    longest = []
    longestSoFar = string[0]
    i = 1

    while i < len(string):
        char = string[i]
        if char not in longestSoFar:
            longestSoFar += char
        else:
            longest.append(longestSoFar)
            longestSoFar = ''
            j = 0
            Idx = 0
            while j < i:
                if string[j] == char:
                    Idx = j
                j += 1
            i = Idx
        i += 1

    length = 0
    for s in longest:
        if len(s) > length:
            i = longest.index(s)
    return longest[i]


if __name__ == '__main__':
    string = {

        "string1": "clementisanarm",
        "string2": "abcbde",

        "string4": "abacacacaaabacaaaeaaafa",
        "string5": "abccdeaabbcddef",
        "string6": "abcdeabcdefc",
        "string7": "abcb",
        "string8": "abc",
        "string9": "a",
        "string0": "clementisacap"
    }
    print(longestSubstringWithoutDuplication(string["string4"]))

    new = {

        "string3": "abcdabcef",
    }
