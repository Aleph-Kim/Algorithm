import sys
n = int(input())

for i in range(1, n + 1):
    print(f"Case #{i}: " + str(sum(map(int, sys.stdin.readline().split()))))