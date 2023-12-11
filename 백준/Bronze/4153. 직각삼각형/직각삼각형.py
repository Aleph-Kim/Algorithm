while True:
    arr = list(map(int, input().split()))

    if sum(arr) == 0:
        break

    a = min(arr)
    c = max(arr)
    arr.remove(a)
    arr.remove(c)
    b = arr[0]
    
    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')