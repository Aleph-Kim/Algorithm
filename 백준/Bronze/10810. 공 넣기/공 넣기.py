n, m = map(int, input().split())

arr = [0] * n

for _ in range(0, m):
    i, j, k = map(int, input().split())
    for n2 in range(i - 1, j):
        arr[n2] = k

print(' '.join(map(str, arr)))
