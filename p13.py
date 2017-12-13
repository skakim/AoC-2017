direction = [1 for _ in range(91)]
ranges = [0 for _ in range(91)]
for _ in range(43):
  inp = list(map(int,input().strip().split(":")))
  ranges[inp[0]] = inp[1]
scanners = [0 if ranges[i] != 0 else -1 for i in range(91)]

#part1
severity = 0
for i in range(91):
  if scanners[i] == 0:
    severity += (i * ranges[i])
  for s in range(91):
    if ranges[s] != -1:
      if scanners[s] + direction[s] not in range(0,ranges[s]):
        direction[s] = - direction[s]
      scanners[s] += direction[s]
print(severity)

#part2
def scanner(rang, step):
    offset = step % ((rang-1) * 2)
    if offset > rang-1:
      return 2*(rang-1)-offset
    else:
      return offset

caught = True
delay = 0
while(caught):
  delay += 1
  caught = False
  for i in range(91):
    if(scanner(ranges[i],delay+i)) == 0:
      caught = True
      break
print(delay)
