def minNumberOfCoinsForChange(n, denoms):
    if n == 0:
        return []
    if n < 0:
        return None

    minCoins = 0
    cur_min = None
    for coin in denoms:
        remainder = n - coin
        current = minNumberOfCoinsForChange(remainder, denoms)
        if current is not None:
            new = current + [coin]
            if cur_min is None or len(new) < len(cur_min):
                minCoins = len(new)
                cur_min = new

    return minCoins


print(minNumberOfCoinsForChange(6, [5, 1, 6]))
