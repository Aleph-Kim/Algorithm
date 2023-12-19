import sys
input = sys.stdin.readline

cnt_arr = [0] * 10001
N = int(input())

for _ in range(N):
    cnt_arr[int(input())] += 1

for i in range(len(cnt_arr)):
    for _ in range(cnt_arr[i]):
        print(i)