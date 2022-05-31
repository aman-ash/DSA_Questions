def solution(S):
    array = list(S)
    found = True

    while True:
        if not found:
            break

        found = False
        for i in range(len(array) - 1):
            AB = array[i] == "A" and array[i + 1] == "B"
            BA = array[i] == "B" and array[i + 1] == "A"
            CD = array[i] == "C" and array[i + 1] == "D"
            DC = array[i] == "D" and array[i + 1] == "C"

            if AB or BA or CD or DC:
                array[i] = array[i + 1] = ''
                found = True
                break
            
        newS = "".join(array)
        array = list(newS)
    return "".join(array)


print(solution("CBACD"))