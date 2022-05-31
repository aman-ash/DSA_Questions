def weightCapacity(weights, maxCapacity):
    i, j = 0, len(weights) - 1
    weights.sort()
    prevSum = weights[-1]
    diff = float("inf")
    while i < j:
        if weights[i] + weights[j] == maxCapacity:
            return maxCapacity
        
        if weights[i] + weights[j] > maxCapacity:
            if abs(maxCapacity - weights[i]+weights[j]) < diff:
                prevSum = weights[i] + weights[j]
                diff = abs(maxCapacity - weights[i]+weights[j])
            j -= 1
        
        elif weights[i] + weights[j] < maxCapacity:
            if abs(maxCapacity - weights[i]+weights[j]) < diff:
                prevSum = weights[i] + weights[j]
                diff = abs(maxCapacity - weights[i]+weights[j])
            i += 1
    return prevSum
            