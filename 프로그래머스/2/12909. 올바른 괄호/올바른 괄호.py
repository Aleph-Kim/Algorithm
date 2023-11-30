def solution(s):
    cnt1 = 0
    cnt2 = 0
    
    for str in s:
        if str == ')':
            cnt1 += 1
        else:
            cnt2 += 1
        
        if cnt2 < cnt1:
            return False
    
    if cnt2 != cnt1:
        return False

    return True