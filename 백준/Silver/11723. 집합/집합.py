import sys
input = sys.stdin.readline
arr = []

for _ in range(int(input())):
    arr2 = input().split()
    s = arr2[0]
    i = int(arr2[1]) if len(arr2) > 1 else 0

    match s:
        case 'add':
            if i not in arr:
                arr.append(i)
        case 'remove':
            if i in arr:
                arr.remove(i)
        case 'check':
            print(1 if i in arr else 0)
        case 'toggle':
            if i in arr:
                arr.remove(i)
            else:
                arr.append(i)
        case 'all':
            arr = list(range(1, 21))
        case 'empty':
            arr = []
