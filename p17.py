buff = [0]
steps = 312

#part1
curr_pos = 0
for v in range(1,2018):
  i = ((curr_pos + steps) % len(buff)) + 1
  buff.insert(i,v)
  curr_pos = i
print(buff[curr_pos+1])

#part2
curr_pos = 0
index1_value = -1
for v in range(1,50000001):
  i = ((curr_pos + steps) % v) + 1
  if i == 1:
    index1_value = v
  curr_pos = i
print(index1_value)
