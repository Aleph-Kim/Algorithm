import sys
n = int(input())

for _ in range(1, n + 1):
    print(sum(map(int, sys.stdin.readline().split())))