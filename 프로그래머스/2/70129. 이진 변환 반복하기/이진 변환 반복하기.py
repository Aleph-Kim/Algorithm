def solution(s):
    i = 0
    cnt = 0
    while(True):
        print(s)
        cnt += int(s.count('0'))
        s = bin(len(s.replace('0', ''))).lstrip('0b')
        i += 1
        
        if s == "1":
            break;
        
    return [i, cnt]