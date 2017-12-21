from math import sqrt

def flip(m, direction): #direction = vertical/horizontal
  if direction == 'vertical':
    if len(m) == 2:
      return [[m[0][1], m[0][0]], [m[1][1], m[1][0]]]
    else:
      return [[m[0][2], m[0][1], m[0][0]], [m[1][2], m[1][1], m[1][0]], [m[2][2], m[2][1], m[2][0]]]
  else:
    if len(m) == 2:
      return [[m[1][0], m[1][1]], [m[0][0], m[0][1]]]
    else:
      return [[m[2][0], m[2][1], m[2][2]], [m[1][0], m[1][1], m[1][2]], [m[0][0], m[0][1], m[0][2]]]

def spin(m):
  if len(m) == 2:
    return [[m[1][0], m[0][0]], [m[1][1], m[0][1]]]
  else:
    return [[m[2][0], m[1][0], m[0][0]], [m[2][1], m[1][1], m[0][1]], [m[2][2], m[1][2], m[0][2]]]
    
def m2str(m):
  s = ""
  for l in m:
    s += "".join(l)
    s += "/"
  return s[:-1]
  
def str2m(s):
  m = []
  for ss in s.split("/"):
    m.append(list(ss))
  return m
  
def split(m):
  sm = []
  if len(m) % 2 == 0:
    for i in range(len(m)//2):
      for j in range(len(m)//2):
        sm.append(m2str([[m[(i*2)][(j*2)],m[(i*2)][(j*2)+1]],[m[(i*2)+1][(j*2)],m[(i*2)+1][(j*2)+1]]]))
  else:
    for i in range(len(m)//3):
      for j in range(len(m)//3):
        sm.append(m2str([[m[(i*3)][(j*3)],m[(i*3)][(j*3)+1],m[(i*3)][(j*3)+2]],[m[(i*3)+1][(j*3)],m[(i*3)+1][(j*3)+1],m[(i*3)+1][(j*3)+2]],[m[(i*3)+2][(j*3)],m[(i*3)+2][(j*3)+1],m[(i*3)+2][(j*3)+2]]]))
  return(sm)

def join(lm, old_len):
  if old_len % 2 == 0:
    new_len = (old_len//2)*3
    nm = [[0]*new_len for _ in range(new_len)]
    per_line = int(sqrt(len(lm)))
    for m in range(len(lm)):
      mx = str2m(lm[m])
      for i in range(len(mx)):
        for j in range(len(mx)):
          nm[((m//per_line)*3)+i][((m%per_line)*3)+j]  = mx[i][j]
  else:
    new_len = (old_len//3)*4
    nm = [[0]*new_len for _ in range(new_len)]
    per_line = int(sqrt(len(lm)))
    for m in range(len(lm)):
      mx = str2m(lm[m])
      for i in range(len(mx)):
        for j in range(len(mx)):
          nm[((m//per_line)*4)+i][((m%per_line)*4)+j]  = mx[i][j]
  return nm
  
  

rules = {}
for _ in range(108):
  rule = input().replace(" ","").split("=>")
  m = str2m(rule[0])
  for _ in range(4):
    m = spin(m)
    rules[m2str(m)] = rule[1]
    rules[m2str(flip(m,'vertical'))] = rule[1]
    rules[m2str(flip(m,'horizontal'))] = rule[1]

curr_m = [['.','#','.'],['.','.','#'],['#','#','#']]
for it in range(18):
  sm = split(curr_m)
  nm = []
  for ssm in sm:
    nm.append(rules[ssm])
  curr_m = join(nm, len(curr_m))
  if it == 4:
    print(m2str(curr_m).count("#"))
print(m2str(curr_m).count("#"))
