wide, height = map(int, raw_input().split(" "))
dom = 0

if wide % 2 == 0:
    dom = (wide/2) * height
else:
    dom = (wide/2) * height + height/2

print dom