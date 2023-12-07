x = list(map(int, input().split()))

if sorted(x) == x:
    print('ascending')
elif list(reversed(sorted(x))) == x:
    print('descending')
else:
    print('mixed')