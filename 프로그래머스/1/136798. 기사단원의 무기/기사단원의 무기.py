def solution(number, limit, power):
    answer = [1]
    for i in range(2, number + 1):
        temp = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i == j * j:
                temp += 1
            elif i % j == 0:
                temp += 2
        
        if temp > limit:
            temp = power
        answer.append(temp)
    return sum(answer)