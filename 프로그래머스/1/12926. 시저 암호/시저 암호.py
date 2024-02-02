def solution(s, n):
    answer = ''
    for c in list(s):
        if c == ' ':
            answer += c
            continue
            
        o = ord(c)
        on = o + n
        
        if (o >= 65 and o <= 90 and on > 90) or (o >= 97 and on > 122):
            on -= 26
        answer += chr(on)
    
    return answer