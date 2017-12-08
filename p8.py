import sys

regs = {}
max_value = - sys.maxsize 
for _ in range(1000):
  l = input()
  instr = l.split(" ")
  if instr[0] not in regs.keys():
    regs[instr[0]] = 0
  if instr[4] not in regs.keys():
    regs[instr[4]] = 0
    
  if_clause = str(regs[instr[4]]) + instr[5] + instr[6] 
  if eval(if_clause):
    if instr[1] == 'inc':
      regs[instr[0]] += int(instr[2])
    else:
      regs[instr[0]] -= int(instr[2])
  
  #part2
  max_value = max(max_value,regs[instr[0]])

#part1
print(max(regs.values()))

#part2
print(max_value)
  
