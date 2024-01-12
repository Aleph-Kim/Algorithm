def solution(arr, divisor):
    arr2 = []
    for i in arr:
        if i % divisor == 0: 
            arr2.append(i)
    return sorted(arr2) if arr2 else [-1]