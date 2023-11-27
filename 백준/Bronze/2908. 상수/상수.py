a, b = list(map(list, map(reversed, map(list, input().split()))))
print(int(''.join(a)) if int(''.join(a)) > int(''.join(b)) else int(''.join(b)))