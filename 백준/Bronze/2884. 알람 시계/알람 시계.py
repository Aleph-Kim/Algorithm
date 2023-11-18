h, m = map(int, input().split())

full_minute = h * 60 + m

alarm_minute = full_minute - 45
h = alarm_minute // 60
if (h < 0):
    h = 24 + h
m = alarm_minute % 60

print(f"{h} {m}")
