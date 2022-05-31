def numToString(num):
    if num <= 26:
        return 'Z' if num == 0 else chr(num + 64)
    
    temp = num // 26
    return chr(temp + 64) + numToString(num%26)
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    print(numToString(27))
    print(numToString(52))
    print(numToString(53))