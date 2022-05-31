def main(string, c):
    count = 0

    for s in string:
        if s == c:
            count += 1
    return count


s = input()
c = input()
print(main(s, c))
