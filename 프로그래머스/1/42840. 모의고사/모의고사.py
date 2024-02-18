def solution(answers):
    answer = []
    score = [0, 0, 0]
    q = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for i in range(len(answers)):
        if q[0][i%5] == answers[i]:
            score[0] += 1
        if q[1][i%8] == answers[i]:
            score[1] += 1
        if q[2][i%10] == answers[i]:
            score[2] += 1
    
    m = max(score)
    for i in range(len(score)):
        if score[i] == m:
            answer.append(i+1)
    
    print(score)
    return answer