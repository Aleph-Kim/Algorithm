fec = 1
for i in range(1, int(input())+1):
    fec *= i

fec_arr = list(str(fec))
fec_arr.reverse()

cnt = 0
for i in fec_arr:
    if i != '0':
        break
    cnt += 1

print(cnt)