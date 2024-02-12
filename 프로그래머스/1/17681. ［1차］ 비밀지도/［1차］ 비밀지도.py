def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        a = list(reversed(bin(a).lstrip('0b')))
        b = list(reversed(bin(b).lstrip('0b')))
        
        if len(a) < n:
            a += list('0'*(n-len(a)))
        if len(b) < n:
            b += list('0'*(n-len(b)))
        
        s = ''
        
        for x,y in zip(a, b):
            if int(x) or int(y):
                s += '#'
            else:
                s += ' '
        answer.append(''.join(reversed(s)))
    return answer