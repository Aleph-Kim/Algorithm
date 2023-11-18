h, m = map(int, input().split())
e = int(input())

alarm_minute = h * 60 + m + e

h = alarm_minute // 60
if (h >= 24):
    h -= 24
m = alarm_minute % 60

print(f"{h} {m}")