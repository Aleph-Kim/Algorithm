def solution(n):
    answer = []
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            nn = n[i] + n[j]
            if nn not in answer:
                answer.append(nn)
    return sorted(answer)