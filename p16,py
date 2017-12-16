import string

def spin(l, n):
    return l[-n:] + l[:-n]

dance1 = input().split(',')

line1 = [list(string.ascii_lowercase)[i] for i in range(16)]
line2 = line1[:]

def dancing(line,dance,repetitions):
  mem = []
  for rep in range(repetitions):
    if ''.join(line) in mem: #cycle detection -> return where in the cycle is the end
      return mem[repetitions % rep]
    mem.append(''.join(line))
    for move in dance:
      if move[0] == 's':
        line = spin(line,int(move[1:]))
        
      elif move[0] == 'x':
        index1,index2 = list(map(int,move[1:].split("/")))
        line[index1], line[index2] = line[index2], line[index1]
      
      elif move[0] == 'p':
        l1,l2 = list(move[1:].split("/"))
        index1 = line.index(l1)
        index2 = line.index(l2)
        line[index1], line[index2] = line[index2], line[index1]

  return line

#part1
print(''.join(dancing(line1,dance1,1)))

#part2
print(''.join(dancing(line2,dance1,1000000000)))
