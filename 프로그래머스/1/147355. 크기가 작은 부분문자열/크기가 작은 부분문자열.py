def solution(t, p):
    cnt = 0
    
    for i in range(len(t) + 1 - len(p)):
        j = int(''.join(list(t[i + k] for k in range(len(p)))))
        if int(p) >= j:
            cnt += 1
            
    return cnt