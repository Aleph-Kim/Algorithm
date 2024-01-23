def solution(arr1, arr2):
    r1 = []
    for i in range(len(arr1)):
        r2 = []
        for j in range(len(arr1[i])):
            r2.append(sum([arr1[i][j], arr2[i][j]]))
        r1.append(r2)
    return r1