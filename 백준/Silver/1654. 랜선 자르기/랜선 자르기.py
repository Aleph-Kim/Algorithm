import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cable = [int(input()) for _ in range(k)]

start = 1
end = max(cable)

while end >= start:
    mid = (start + end) // 2
    cnt = [i // mid for i in cable]
    
    if sum(cnt) >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)