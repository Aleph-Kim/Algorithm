N = int(input())

arr = [input().split() for _ in range(N)]

arr.sort(key=lambda x: int(x[0]))

for x in arr:
    print(x[0], x[1])