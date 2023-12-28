a, b = map(int, input().split())

a_arr = []
small_int = min(a, b)
big_int = max(a, b)

for i in range(1, a + 1):
    if (a % i == 0):
        a_arr.append(i)
        
for i in reversed(range(1, b + 1)):
    if (b % i == 0) and i in a_arr:
        print(i)
        break

loop_cnt = 1
while True:
    if small_int * loop_cnt % big_int == 0:
        print(small_int * loop_cnt)
        break
    loop_cnt += 1