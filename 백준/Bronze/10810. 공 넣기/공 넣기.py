n, m = map(int, input().split())

arr = list(["0" for _ in range(n)])

for _ in range(0, m):
    i, j, k = map(int, input().split())
    for n2 in range(i - 1, j):
        arr[n2] = str(k)

print(' '.join(arr))
