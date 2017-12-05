instr1 = []
instr2 = []
for _ in range(1074):
  n = int(input())
  instr1.append(n)
  instr2.append(n)

#part 1
pos = 0
counter = 0
while (pos >= 0 and pos < len(instr1)):
  counter += 1
  jmp = instr1[pos]
  instr1[pos] += 1
  pos += jmp
print(counter)

#part 2
pos = 0
counter = 0
while (pos >= 0 and pos < len(instr2)):
  counter += 1
  jmp = instr2[pos]
  if instr2[pos] >= 3:
    instr2[pos] -= 1
  else:
    instr2[pos] += 1
  pos += jmp
print(counter)
