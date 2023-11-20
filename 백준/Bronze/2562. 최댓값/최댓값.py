arr = []
for i in range(9):
    arr.insert(i, int(input()))
    
m = max(arr)
print(m)
print(arr.index(m) + 1)