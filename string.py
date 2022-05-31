def string(str1, str2, str3):
    answer = []
    Idx = 0
    while Idx < len(str1) and Idx < len(str2) and Idx < len(str3):
        if str1[Idx] != str2[Idx] or str1[Idx] != str3[Idx]:
            break
        answer.append(str1[Idx])
        Idx += 1
    return ''.join(answer)


if __name__ == "__main__":
    str1 = "floaer"
    str2 = "floatnoat"
    str3 = "floa"
    print(string(str1, str2, str3))
