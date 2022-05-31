def balancedBrackets(string):
    openBraces = []
    for b in string:
        if b == "(" or b == "{" or b == "[":
            openBraces.append(b)
        elif b == ")" or b == "}" or b == "]":
            if len(openBraces):
                close = openBraces.pop()
                if close == ")" or close == "}" or close == "]":
                    return False
            else:
                return False
        else:
            pass

    if len(openBraces):
        return False
    return True


if __name__ == "__main__":
    string = '{[[[[({(}))]]]]}'
    print(balancedBrackets(string))
