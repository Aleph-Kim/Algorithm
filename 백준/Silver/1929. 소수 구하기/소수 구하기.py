M, N = map(int, input().split())

for i in range(M if M > 1 else 2, N + 1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
