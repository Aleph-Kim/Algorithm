a = int(input())
b = int(input())
bList = list(map(int, str(b)))

print(a * bList[-1])
print(a * bList[-2])
print(a * bList[-3])
print(a * b)