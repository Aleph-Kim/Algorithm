import sys
input = sys.stdin.readline

N = int(input())
arr = []
counts = {}

for _ in range(N):
    i = int(input())
    arr.append(i)
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

arr.sort()
print(round(sum(arr) / N))
print(arr[int(N/2)])

most_cnt = max(counts.values())
most_counts = []
for cnt in counts.items():
    k, v = cnt
    if v == most_cnt:
        most_counts.append(k)

if len(most_counts) > 1:
    print(sorted(most_counts)[1])
else:
    print(most_counts[0])
    
print(len(range(min(arr), max(arr))))
