inp = list(raw_input())
line = []

for i in range(0, len(inp)):
    if inp[i] != "+":
        line.append(inp[i])

line.sort()
print "+".join(line)

