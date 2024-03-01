import sys
input = sys.stdin.readline
N = int(input())

i = 1
while (True):
    temp = i + sum(map(int, list(str(i))))

    if (temp == N):
        break
    
    if (i > N):
        i = 0
        break
    i += 1
print(i)
