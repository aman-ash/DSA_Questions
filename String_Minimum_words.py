def minimumCharactersForWords(words):
    answer = {}

    for word in words:
        temp = {}
        for char in word:
            if char in temp:
                temp[char] += 1
            else:
                temp[char] = 1
        for key, value in temp.items():
            if key in answer:
                if answer[key] >= temp[key]:
                    pass
                else:
                    answer[key] += temp[key] - answer[key]
            else:
                answer[key] = value
    ans = ''
    for key, value in answer.items():
        ans += key * value
    return list(ans)


if __name__ == "__main__":
    words = ["this", "that", "did", "deed", "them!", "a"]
    print(minimumCharactersForWords(words))
