import sys
input = sys.stdin.readline
arr = []

for _ in range(int(input())):
    arr2 = input().split()

    match arr2[0]:
        case 'push':
            arr.append(arr2[1])
        case 'pop':
            print(arr.pop(0) if arr else -1)
        case 'size':
            print(len(arr))
        case 'empty':
            print(0 if arr else 1)
        case 'front':
            print(arr[0] if arr else -1)
        case 'back':
            print(arr[len(arr) - 1] if arr else -1)