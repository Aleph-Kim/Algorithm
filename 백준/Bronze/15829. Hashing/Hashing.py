input()

arr = list('abcdefghijklmnopqrstuvwxyz')
str_arr = list(input())
total = 0
for i in range(len(str_arr)):
    total += (arr.index(str_arr[i]) + 1) * (31 ** i)
print(total % 1234567891)