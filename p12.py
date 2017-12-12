conn = {x:[] for x in range(2000)}

for _ in range(2000):
  info = input().split("<->")
  a = int(info[0])
  temp = list(map(int,info[1].split(",")))
  for b in temp:
    conn[a].append(b)
    conn[b].append(a)

#part 1
nexts = [0]
visited = set()
while nexts:
  x = nexts.pop()
  for y in conn[x]:
    if y not in visited:
      visited.add(y)
      nexts.append(y)
    
print(len(visited))

#part 2
groups = 0
visited = set()
for z in range(2000):
  if z in visited:
    continue
  groups += 1
  group = [z]
  while group:
    x = group.pop()
    for y in conn[x]:
      if y not in visited:
        visited.add(y)
        group.append(y)

print(groups)
