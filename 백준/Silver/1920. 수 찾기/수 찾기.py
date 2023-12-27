_ = input()
arr = set(map(int, input().split()))
_ = input()

for i in list(map(int, input().split())):
    if i in arr:
        print(1)
    else:
        print(0)