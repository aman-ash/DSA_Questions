def find(N, arr):
    ans = 0
    if len(arr) < 2:
        return 1 if (arr[0] ** arr[0]) % 2 == 0 else 0
    for i in range(N):
        for j in range(i, N):
            if arr[i] == arr[j] and arr[i] % 2 == 0:
                ans += 1
                continue
            sums = helper(arr[i]*arr[j])

        for s in sums:
            if (s[0] ** s[1]) % 2 == 0 or (s[1] ** s[0]) % 2 == 0:
                ans += 1
                break
    return ans


def sum_of_primes(num):
    isPrime = 1
    for i in range(2, int(num/2), 1):
        if(num % i == 0):
            isPrime = 0
            break
    return isPrime


def helper(num):
    primeNumbers = []
    flag = 0
    i = 2
    for i in range(2, int(num/2), 1):
        if(sum_of_primes(i) == 1):
            if(sum_of_primes(num-i) == 1):
                primeNumbers.append([i, num-i])
                flag = 1
    return primeNumbers


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for i in range(N)]
    result = find(N, A)
    print(result)
