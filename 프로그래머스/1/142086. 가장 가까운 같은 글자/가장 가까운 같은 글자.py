def solution(s):
    a = ''
    answer = []
    for i in range(len(s)):
        f = a.rfind(s[i])
        
        if f == -1:
            answer.append(f)
        else:
            answer.append(i - f)
        
        a += s[i]
    return answer