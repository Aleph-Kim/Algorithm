def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        last = ''
        while(True):
            if s == '':
                answer += 1
                break

            for w in arr:
                if last != w and s[:len(w)] == w:
                    s = s[len(w):]
                    last = w
                    break
            else:
                break
        
    return answer