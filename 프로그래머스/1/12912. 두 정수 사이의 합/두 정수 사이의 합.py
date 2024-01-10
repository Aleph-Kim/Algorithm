def solution(a, b):
    arr = [a, b]
    arr.sort()
    return sum(range(arr[0], arr[1]+1))