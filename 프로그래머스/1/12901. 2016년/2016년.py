def solution(a, b):
    w = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = w[(sum(m[:a-1]) + b) % 7 - 1]
          
    return answer