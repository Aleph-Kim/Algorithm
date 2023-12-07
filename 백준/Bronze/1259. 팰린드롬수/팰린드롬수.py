while (1):
    x = input()
    if x == '0':
        break
    print('yes') if x[::-1] == x else print('no')