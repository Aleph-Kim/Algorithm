def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(1, len(score) + 1):
        if i % m == 0:
            answer += score[i-1] * m
    return answer