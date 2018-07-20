line1 = raw_input()
line2 = raw_input()

line1 = list(line1.lower())
line2 = list(line2.lower())

def compare():
    for i in range (0, len(line1)):
        if line1[i] == line2[i]:
            continue
        elif line1[i] < line2[i]:
            return -1
        elif line1[i] > line2[i]:
            return 1
    return 0

print compare()
