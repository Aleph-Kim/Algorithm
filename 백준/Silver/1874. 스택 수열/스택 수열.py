import sys
input = sys.stdin.readline

n = int(input())
stack = []
cur = 1
answer = []
flag = True

for i in range(n):
    num = int(input())
    
    while cur <= num:
        stack.append(cur)
        cur += 1
        answer.append('+')
        
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = False
        exit

if flag:
    for s in answer:
        print(s)
else:
    print('NO')