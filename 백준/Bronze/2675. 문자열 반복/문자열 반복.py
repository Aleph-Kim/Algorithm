t = int(input())

for i in range(t):
    t2, s = input().split()
    for c in list(s):
        print(c*int(t2), end="")
    print()