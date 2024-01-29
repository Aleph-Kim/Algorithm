def solution(s):
    str = ''
    r = 0
    for i in range(len(s)):
        if s[i] == ' ' and i % 2 == r:
            if r == 0:
                r = 1
            else:
                r = 0
        str += s[i].upper() if i % 2 == r else s[i].lower()
    return str