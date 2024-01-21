def solution(price, money, count):
    n = 0
    for i in range(1, count + 1):
        n += (price * i)
    return  n - money if n > money else 0