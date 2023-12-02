def solution(A,B):
    s = 0
    A.sort()
    B.sort()
    B.reverse()
    for i in range(len(A)):
        s += A[i] * B[i]
    return s