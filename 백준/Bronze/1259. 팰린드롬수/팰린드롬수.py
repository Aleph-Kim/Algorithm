while (True):
    x = input()
    if x == '0':
        break
    print('yes') if str(''.join(list(reversed(x)))) == x else print('no')