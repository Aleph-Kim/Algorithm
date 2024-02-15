import sys
input = sys.stdin.readline

N, k = map(int, input().split())
arr = list(range(1, N+1))
result = []

for _ in range(1, N+1):
    n = (k - 1) % len(arr)
    result.append(str(arr.pop(n)))
    arr = arr[n:] + arr[:n]

print('<' + ', '.join(result) + '>')
