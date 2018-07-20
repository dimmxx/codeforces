length = int(raw_input())
op = []

for i in range(length):
    data = str(raw_input())
    op.append(data.upper())

#length = 3
#op = ["X++", "X--", "x++"]
#print op

x = 0
for i in range (length):
    if op[i] == "X++" or op[i] == "++X":
        x += 1
    elif op[i] == "X--" or op[i] == "--X":
        x -= 1

print x