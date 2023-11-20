arr = [*range(31)]
del (arr[0])

for _ in range(28):
    del (arr[arr.index(int(input()))])

arr.sort()
print(arr[0])
print(arr[1])
