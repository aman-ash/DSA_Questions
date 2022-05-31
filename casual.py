arr = [['bman', 1], ['aman', 2], ['mahore', 1], ['bman', 0]]
ans2 = sorted(arr, key=lambda x: (x[0], x[1]))
ans3 = sorted(sorted(arr, key=lambda x: x[1]), key=lambda x: x[0])

print(ans2)
print(ans3)
