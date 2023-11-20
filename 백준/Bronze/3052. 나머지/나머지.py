arr = []

for _ in range(10):
    j = int(input()) % 42
    arr.append(j)

print(len(set(arr)))