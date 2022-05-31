def search(pat, txt):
    count = 0
    P = len(pat)
    T = len(txt)
    i = 0

    while i <= T - P:
        current = txt[i:i+P]
        no = 0
        for w in current:
            if w in pat:
                no += 1

        if no == P:
            count += 1
        i += 1

    return count


if __name__ == '__main__':
    txt = 'forxxorfxdofr'
    pat = 'for'
    print(search(pat, txt))
