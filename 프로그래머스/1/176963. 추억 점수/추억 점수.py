def solution(name, yearning, photo):
    answer = []
    for peoples in photo:
        s = 0
        for people in peoples:
            s += yearning[name.index(people)] if people in name else 0
        answer.append(s)
    return answer