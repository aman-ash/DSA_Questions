def func(s):
    num = ''
    for w in s:
        if w:
            num += '0'
        else:
            num += '1'
    
    num = int(num, 2)
    ans = int(str_base(num, 6))
    res = []
    while ans > 0:
        res.append(ans % 10)
        ans //= 10
    return res
    
    
def str_base(val, base):
    res = ''
    while val > 0:
        res = str(val % base) + res
        val //= base 
    if res: return res
    return '0'



print(func([False, False, True, True]))
print(str_base(16,6))