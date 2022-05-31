import random


def solution(value):
    for letter in value:
        if value == letter*len(value):
            return "IMPOSSIBLE"
    newWord = ''
    for i in range(len(value)):
        pos = random.randint(0, len(value)-1)
        newWord += value[pos]
        value = value[:pos] + value[pos+1:]
    return newWord


t = int(input())
case = 1
while t > 0:
    value = str(input())
    print("Case #"+str(case) + ": " + solution(value))

    t -= 1
    case += 1
