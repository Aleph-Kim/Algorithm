n, m = map(int, input().split())

arr = [n for n in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp1 = arr[i - 1]
    tmp2 = arr[j - 1]
    arr[i - 1] = tmp2
    arr[j - 1] = tmp1

print(' '.join(map(str, arr)))
