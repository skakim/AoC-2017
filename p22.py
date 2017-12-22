inp = []
for _ in range(25):
  inp.append(list(input()))
  
mx = {}
for x in range(len(inp)):
  for y in range(len(inp)):
    mx[(x,y)] = (2 if inp[x][y]=='#' else 0)
print(mx)

move = [(-1,0), (0,1), (1,0), (0,-1)]
pos = ((len(inp))//2,(len(inp))//2)
d = 0
infected = 0
for i in range(10000000):
  #print(pos,mx[pos],direction,end=' => ')
  if mx[pos]==0:
    d = (d-1)%4
    mx[pos]=1
  elif mx[pos]==1:
    mx[pos]=2
    #if not(pos[0] in range(len(pos)) and pos[1] in range(len(pos))):
    #  infected += 1
    #elif inp[pos[0]][pos[1]] != '#':
    #  infected += 1
    infected += 1
  elif mx[pos]==2:
    d = (d+1)%4
    mx[pos]=3
  elif mx[pos]==3:
    d = (d+2)%4
    mx[pos]=0
  #print(pos,mx[pos],direction)
  pos = tuple(map(sum,zip(pos,move[d])))
  if pos not in mx.keys():
    mx[pos] = 0
  
  if i % 100000 == 0:
    print(i)

print(infected)
