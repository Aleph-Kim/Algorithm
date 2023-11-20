arr = [*range(1, 31)]

for _ in range(28):
    arr.remove(int(input()))

for n in arr:
    print(n)