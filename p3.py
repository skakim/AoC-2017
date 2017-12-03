n = int(input())

#part 1
size = 1
while(size*size < n):
  size += 2

corners = [size*size - k*(size-1) for k in range(4)]

for corner in corners:
  dist = abs(corner-n)
  if dist <= (size-1)//2:
    print(size-1-dist)
    break

#part 2
neighborhood = [(-1, 0), (1, 1), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, -1), (1, 0)]
matrix = {}
x = 0
y = 0
dx = 0
dy = -1
total = 0
while total <= n:
  total = 0
  for neighbor in neighborhood:
    nx,ny = neighbor
    if (x+nx,y+ny) in matrix:
      total += matrix[(x+nx,y+ny)]
  if (x,y) == (0,0):
    matrix[(0,0)] = 1
  else:
    matrix[(x,y)] = total
  if (x == y) or (x > 0 and x == 1-y) or (x < 0 and x == -y): #see if turns
    dx, dy = -dy, dx
  x, y = x+dx, y+dy
print(total)
