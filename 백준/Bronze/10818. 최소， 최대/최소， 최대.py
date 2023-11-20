import sys
input = sys.stdin.readline
_ = input()
a = list(map(int, input().split()))

print(min(a), max(a))