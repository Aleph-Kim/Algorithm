n, m = map(int, input().split())
arr = [*range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    arr[i:j] = list(reversed(arr[i:j]))

print(*arr)
