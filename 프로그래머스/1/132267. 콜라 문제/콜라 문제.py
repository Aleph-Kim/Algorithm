def solution(a, b, n):
    answer = 0
    while n >= a:
        i = n // a * b
        n = i + n % a
        answer += i
    return answer