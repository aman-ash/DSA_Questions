from math import sqrt

def solve(n):
    
    def valid(i):
        pass

    if n < 5:
        return 0
    arr = getPrime(n)
    count = 0
    for i in arr:
        if valid(i):
            count += 1
    return count

def getPrime(n):
    prime = []
    for val in range(2, n+1):
        flag = True
        for i in range(2, int(sqrt(n)) + 1):
            if val % i == 0:
                flag = False
                break
        if flag:
            prime.append(val)
    return prime




if __name__ == '__main__':
    print(solve(int(input())))
    print(len(getPrime(int(input()))))
       