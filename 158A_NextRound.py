
contestent, place = map(int, raw_input().split(" "))
score = map(int, raw_input().split(" "))
total = 0

if place == contestent and score[place - 1] != 0:
    total = place

for i in range(0, len(score)):
     if score[i] == 0 and i < place:
         total = i
         print total
         exit(0)

for i in range(place - 1, len(score) - 1):

    if score[i] > score[i + 1]:
        total = i + 1
        break
    elif score[i] == score[i + 1] and i != len(score) - 2:
        next
    elif score[i] == score[i + 1] and i == len(score) - 2:
        total = i + 2
        next

print total
