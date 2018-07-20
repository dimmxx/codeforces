# 0  1  2  3  4
# B  R  R  G  G

l = int(raw_input())
line = raw_input()

#line = "RRRRR"

line = list(line)
count = 0
length = len(line)



while count <= (l - 2):
    if line[count] != line[count + 1]:
        count += 1

    else:
        del line[count + 1]
        l -= 1

print length - l


