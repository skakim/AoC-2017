def reverse_sublist(lst,start,end):
    sublist = []
    for i in range(start,end+1):
      sublist.append(lst[i % len(lst)])
    reverse = list(reversed(sublist))
    j=0
    for i in range(start,end+1):
      lst[i % len(lst)] = reverse[j]
      j+=1
    
    return lst

def gen_hash(inp):
  lengths = []
  for c in inp:
    lengths.append(ord(c))
  for i in [17, 31, 73, 47, 23]:
    lengths.append(i)
  numbers = [x for x in range(0,256)]
  curr_pos = 0
  skip_size = 0
  
  for _ in range(64):
    for l in lengths:
      numbers = reverse_sublist(numbers,curr_pos,curr_pos+l-1)
      curr_pos += (l+skip_size)
      skip_size += 1
  
  dense_list = []
  for i in range(16):
    for j in range(16):
      if j == 0:
        acc = numbers[(i*16) + j]
      else:
        acc = acc ^  numbers[(i*16) + j]
    dense_list.append(acc)
  
  final = ""
  for x in dense_list:
    h = hex(x)[2:]
    if len(h) == 1:
      h = "0"+h
    final += h
  return final

#part1
s = input()
one_counter = 0
dots = []
for i in range(128):
  line = s+"-"+str(i)
  hsh = gen_hash(line)
  binary = bin(int(hsh,16))[2:].zfill(128)
  one_counter += binary.count('1')
  dots += [(i, j) for j, d in enumerate(binary) if d == '1']
print(one_counter)

#part2
groups = 0
while dots:
  queued = [dots[0]]
  while queued:
      (x,y) = queued.pop()
      if (x,y) in dots: #if it is a 1 in (x,y)
          dots.remove((x,y))
          queued += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
  groups += 1
print(groups)
