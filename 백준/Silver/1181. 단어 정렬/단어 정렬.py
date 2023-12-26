import sys
input = sys.stdin.readline

arr = sorted(list(set([input().strip() for _ in range(int(input()))])))
arr.sort(key=lambda x:int(len(x)))

print('\n'.join(arr))
