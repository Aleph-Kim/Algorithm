total = int(input())
n = int(input())

for _ in range(1, n + 1):
    price, cnt = map(int, input().split())
    total -= price * cnt
    
print("Yes" if total == 0 else "No")