x = list(map(int, input().split()))
y = [1, 1, 2, 2, 2, 8]
z = []

for i in range(len(x)):
    z.append(str(y[i] - x[i]))

print(' '.join(z))