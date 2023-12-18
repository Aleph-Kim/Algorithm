import collections
import sys
input = sys.stdin.readline

_ = input()

get_arr = list(map(int, input().split()))
get_count = dict(collections.Counter(get_arr))

_ = input()

search_arr = list(map(int, input().split()))

for i in search_arr:
    cnt = get_count.get(i)
    cnt = 0 if cnt == None else cnt
    print(cnt, end=" ")
