_ = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                cnt += 1
            else:
                break

print(cnt)