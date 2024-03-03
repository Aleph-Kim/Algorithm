n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    arr[i] = arr[i][1], arr[i][0]

arr.sort()

for temp in arr:
    print(temp[1], temp[0])
