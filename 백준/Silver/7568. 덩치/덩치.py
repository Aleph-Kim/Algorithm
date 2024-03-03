n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        
        a,b = arr[i]
        c,d = arr[j]
        
        if a < c and b < d:
            rank += 1
    
    result.append(rank)

print(*result)