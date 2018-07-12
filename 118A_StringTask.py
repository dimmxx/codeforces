line = str(raw_input()).lower()

line_m = []

for i in line:
    if i == "a" or i == "o" or i == "y" or i == "e" or i == "u" or i == "i":
       i = ""
       line_m.append(i)
       next
    else:
       i = "." + i
       line_m.append(i)

print ''.join(line_m)