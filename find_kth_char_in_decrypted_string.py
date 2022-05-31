def kThCharaterOfDecryptedString(s, k):
    nums, strings = [], []
    num = ''
    string = ''

    for i in range(len(s)):
        if s[i].isnumeric():
            num += s[i]
            if string:
                strings.append(string)
                nums.append(num)
                num = ''
            string = ''

        else:
            string += s[i]
            if num:
                nums.append(num)
                strings.append(string)
            num = ''

    temp = ''
    for i in range(len(nums)):
        temp += strings[i] * int(nums[i])

    return temp


if __name__ == '__main__':
    s = 'ab12c3'
    print(kThCharaterOfDecryptedString(s, 20))
