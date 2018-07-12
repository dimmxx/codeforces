lines = int(raw_input())

longword = []

for i in range(0, lines):
      word = raw_input()
      longword.append(word)

def cutter(word):
    word = str(word)
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[len(word) - 1]
    else:
        return word

for item in longword:
    print cutter(item)


