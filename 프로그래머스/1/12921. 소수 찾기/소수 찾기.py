def solution(n):
    arr = [1] * n
    
    for i in list(range(2, n+1)):
        if arr[i-1] == 0:
            continue
        
        j = i * 2
        while(j <= n):
            arr[j-1] = 0
            j += i
        
    return sum(arr) - 1