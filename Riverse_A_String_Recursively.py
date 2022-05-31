def func(s):
    if len(s) <= 1:
        return s

    first = s[0]
    last = s[1:]

    return func(last) + first


if __name__ == '__main__':
    print(func("PYTHON"))
