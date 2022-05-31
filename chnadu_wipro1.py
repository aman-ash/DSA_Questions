def main(num):
    num = list(str(num))
    new = ''
    for i in range(0, len(num) - 1, 2):
        new += max(num[i], num[i+1])

    if i < len(num) - 2:
        new += num[-1]
    return int(new)


s = int(input())
print(main(s))
