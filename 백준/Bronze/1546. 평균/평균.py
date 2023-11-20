m = int(input())
arr = list(map(int, input().split()))

s = 0
for i in arr:
    s += i / max(arr) * 100
print(s/len(arr))
