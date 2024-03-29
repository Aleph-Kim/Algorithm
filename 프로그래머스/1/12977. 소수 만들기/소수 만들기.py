def pnCheck(i):
    for j in range(2, int(i ** 0.5)+1):
        if i == j*j or i % j == 0:
            return False
    
    return True
                
def solution(nums):
    sums = []
    num_len = len(nums)
    for i in range(num_len-2):
        for j in range(i+1, num_len-1):
            for k in range(j+1, num_len):
                sums.append(sum([nums[i], nums[j], nums[k]]))
    pn = []
    
    for i in sums:
        if i in pn:
            pn.append(i)
            continue
            
        if pnCheck(i):
            pn.append(i)

    return len(pn)