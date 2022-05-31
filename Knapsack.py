def knapsack(weights, values, capacity, length, d={}):
    if length == 0:
        return 0
    if length in d:
        return d[length]
    
    if weights[length - 1] <= capacity:

        d[length] = max(values[length - 1] + knapsack(weights, values, capacity - weights[length - 1], length - 1),
                         knapsack(weights, values, capacity, length - 1))
        return d[length]
    
    d[length] =  knapsack(weights, values, capacity, length - 1)
    return d[length]




def knapsack1(weights, values, capacity, length):
    table = [[0 for  weight in range(capacity+1)] for _ in range(length + 1)]

    for size in range(1, length):
        for weight in range(1, capacity):

            if size == 1 or weight == 1:
                continue

            if weights[weight - 1] <= capacity:
                table[size][weight] = max(values[weight - 1] + table[size - 1][capacity - weights[weight - 1]], table[weight][size - 1])

            else:
                table = table[weight][size - 1]
    
    return table[-1][-1]


if __name__ == "__main__":
    values = [1, 4, 5, 6]
    weights = [2, 3, 6, 7]
    capacity = 10
    print(knapsack1(weights, values, capacity,len(weights)))