prog_aboves = {}
prog_weights = {}
for _ in range(1124):
  line = input().split("->")
  prog = line[0].split(" ")
  prog_name = prog[0]
  prog_weight = int(prog[1][1:-1])
  above = []
  if len(line) > 1:
    above = line[1].replace(" ","").split(",")
  prog_aboves[prog_name] = above
  prog_weights[prog_name] = prog_weight

#part1
prog_down = {name:[] for name in prog_aboves.keys()}
for name in prog_aboves.keys():
  l = prog_aboves[name]
  for n in l:
    prog_down[n].append(name)

n = "dsiixv"
while prog_down[n]:
  n = prog_down[n][0]
print(n)
basis = n

#part2

def real_weight(name):
  if len(prog_aboves[name]) == 0:
    return prog_weights[name]
  else:
    aboves_weights = []
    for ab in prog_aboves[name]:
      aboves_weights.append(real_weight(ab))
    if len(set(aboves_weights)) <= 1: #if all equal
      return prog_weights[name] + sum(aboves_weights)
    else: #with the info printed, do manual analysis (see what was different, the weight of the different and calculate what should be its weight)
      print("DIFFERENT!",aboves_weights)
      for ab in prog_aboves[name]:
        print(prog_weights[ab])
      raise

real_weight(basis)
