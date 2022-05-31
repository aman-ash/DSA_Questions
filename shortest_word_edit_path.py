def shortestWordEditPath(source, target, words):
    seen = [False for i in words]

    if target in words:
        target_Idx = words.index(target)
    else:
        return -1

    posibilities = {}
    find_posibilities(words, posibilities)
    counter = 0

    start_Idx = [[]]

    for i, s in enumerate(words):
        if isValid(s, source):
            start_Idx[0].append(i)

    while len(start_Idx):
        current = start_Idx.pop(0)
        for cur in current:
            go_to = posibilities[cur]
            temp = []
            for i in go_to:
                if i == target_Idx:
                    return counter

                if seen[i]:
                    continue
                temp.append(i)
                seen[i] = True
            start_Idx.append(temp)

        counter += 1
    return -1


def find_posibilities(arr, hashmap):
    flag = False
    for i in range(len(arr)):
        for j in range(len(arr)):
            if isValid(arr[i], arr[j]):
                flag = True
                if i in hashmap:
                    hashmap[i].append(j)
                else:
                    hashmap[i] = [j]
            else:
                if not flag:
                    hashmap[i] = []

    return hashmap


def isValid(str1, str2):
    count = 0

    for s in str1:
        if s not in str2:
            count += 1

        if count > 1:
            return False
    return True


if __name__ == '__main__':
    source = "bit"
    target = "dog"
    words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
    print(shortestWordEditPath(source, target, words))

'''
source = "bit", target = "dog"

words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
                         

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.



1 -> use loop to find start point

 seen = [False, True]
 
Sp = [0, 2]


target = 5

posiibilities :    {

    0 : [1]
    1 : [3]

    2 : []

    3 : [4, 1]

    4 : [3, 5]

    5 : [4]

    6 : [3]
    }

root = 3

queue = [5]


time = O(n2) , space = O(n)

'''
