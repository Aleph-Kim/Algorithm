import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    str = list(input().strip())
    open_cnt = 0
    close_cnt = 0
    for i in range(len(str)):
        if str[i] == "(":
            open_cnt += 1
        else:
            close_cnt += 1

        if open_cnt < close_cnt:
            print("NO")
            break

        if i == len(str) - 1:
            if open_cnt == close_cnt:
                print("YES")
            else:
                print("NO")