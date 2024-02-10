def solution(k, score):
    top = []
    answer = []
    for i in score:
        top.append(i)
        top.sort(reverse=True)
        
        if len(top) > k:
            answer.append(top[k-1])
        else:
            answer.append(top[len(top)-1])
    return answer