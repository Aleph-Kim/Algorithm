a, b = map(int, input().split())

while max(a, b) > 0:
    print(a + b)
    a, b = map(int, input().split())