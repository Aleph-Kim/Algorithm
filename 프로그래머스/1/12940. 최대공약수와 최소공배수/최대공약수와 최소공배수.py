def solution(n, m):
    for i in range(n if n > m else m, n * m + 1):
        if i % n == 0 and i % m == 0:
            return [(n * m) // i, i]
