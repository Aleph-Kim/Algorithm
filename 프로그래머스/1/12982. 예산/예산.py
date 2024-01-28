def solution(d, budget):
    cnt = 0
    for i in list(sorted(d)):
        if budget - i > -1:
            budget -= i 
            cnt += 1
    return cnt