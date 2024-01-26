def solution(arr):
    r_arr = []
    x = -1
    for i in range(len(arr)):
        if x == arr[i] and i != len(arr):
            continue
        
        x = arr[i]
        r_arr.append(x)
        
    return r_arr