l = input().split(",")

pos = [0,0,0] #x,y,z -> https://www.redblobgames.com/grids/hexagons/#coordinates-cube

#part2
distances = []

for direction in l:
  if direction == "n":
    pos[1] += 1
    pos[2] -= 1
  elif direction == "s":
    pos[1] -= 1
    pos[2] += 1
  elif direction == "nw":
    pos[0] -= 1
    pos[1] += 1
  elif direction == "se":
    pos[0] += 1
    pos[1] -= 1
  elif direction == "ne":
    pos[0] += 1
    pos[2] -= 1
  elif direction == "sw":
    pos[0] -= 1
    pos[2] += 1
  #part2
  d = sum(abs(x) for x in pos)//2
  distances.append(d)

#part1
print(sum(abs(x) for x in pos)//2)
#part2
print(max(distances))
