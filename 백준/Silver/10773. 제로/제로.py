import sys
input = sys.stdin.readline

K = int(input())
arr = []

for _ in range(K):
    i = int(input())
    if i == 0:
        arr.pop()
    else:
        arr.append(i)

print(sum(arr))
