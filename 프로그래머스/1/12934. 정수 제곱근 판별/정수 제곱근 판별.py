def solution(n):
    i = n ** 0.5
    if i.is_integer() == False:
        return -1
    return (i + 1) ** 2