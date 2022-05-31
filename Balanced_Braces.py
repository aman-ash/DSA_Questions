def isBalanced(s):
    openBraces = '([{'
    stack = []

    for w in s:
        if w in openBraces:
            stack.append(w)
        else:
            if not len(stack):
                return "No"

            A = w == ')' and stack[-1] == '('
            B = w == ']' and stack[-1] == '['
            C = w == '}' and stack[-1] == '{'

            if A or B or C:
                stack.pop()
            else:
                return "NO"

    return "NO" if len(stack) else "YES"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)

