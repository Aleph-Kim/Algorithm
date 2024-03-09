import sys

input = sys.stdin.readline

_ = input()
arr1 = list(map(int, input().split()))
_ = input()
arr2 = list(map(int, input().split()))

_dict = {}

for i in arr1:
    _dict[i] = 0
    
for i in arr2:
    if i in _dict:
        print('1', end=' ')
    else:
        print('0', end=' ')