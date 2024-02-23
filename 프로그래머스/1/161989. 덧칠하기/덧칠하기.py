def solution(n, m, section):
    answer = 0
    arr = [1] * n
    for s in section:
        arr[s-1] = 0
    
    i = 0
    while (i < n):
        if arr[i] == 0:
            arr[i:min([i+m, n-1])] = [1] * min([m, n-i])
            answer += 1
            
        i += 1
    return answer