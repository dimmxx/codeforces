team = list(raw_input())
qua = 7


def danger():
    for player in range (0, len(team) - 2):
        flag = 1
        for i in range (player + 1, len(team)):
             if team[player] == team[i] and flag < qua - 1:
                 flag +=1
                 continue
             elif team[player] == team[i] and flag == qua -1:
                 return "YES"
             elif team[player] != team[i]:
                 break
    return "NO"

print danger()




