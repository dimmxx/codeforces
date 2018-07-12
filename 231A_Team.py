
task = int(raw_input())
taskset = []
for t in range (task):
    data = map(int, raw_input().split(" "))
    taskset.append(data)

total = 0
solve = 0

#taskset = [[1,0,0], [1,1,1], [1,0,0]]

for i in range(0, len(taskset)):
      sum = 0
      for j in range(0, len(taskset[i])):
           sum += taskset[i][j]

      if sum >= 2:
          solve += 1

print solve