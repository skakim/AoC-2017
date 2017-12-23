def get_chars(start, end):
    return ''.join(chr(c) for c in range(ord(start), ord(end)+1))
    
program = []
for _ in range(32):
  program.append(input().split(" "))

registers = {x:0 for x in get_chars('a','h')}
registers['a'] = 1
print(registers)
pc = 0
i = 0

#part2 TODO: optimize input

while(pc in range(32)):
  i += 1
  instr = program[pc][0]
  if instr == 'set':
    r1 = program[pc][1]
    r2 = program[pc][2]
    if r2.isalpha():
      registers[r1] = registers[r2]
    else:
      registers[r1] = int(r2)
    pc += 1
  elif instr == 'sub':
    r1 = program[pc][1]
    r2 = program[pc][2]
    if r2.isalpha():
      registers[r1] -= registers[r2]
    else:
      registers[r1] -= int(r2)
    pc += 1
  elif instr == 'mul':
    r1 = program[pc][1]
    r2 = program[pc][2]
    if r2.isalpha():
      registers[r1] *= registers[r2]
    else:
      registers[r1] *= int(r2)
    pc += 1
  elif instr == 'jnz':
    r1 = program[pc][1]
    r2 = program[pc][2]
    if (r1.isalpha()):
      if registers[r1] != 0:
        if r2.isalpha():
          pc += registers[r2]
        else:
          pc += int(r2)
      else:
        pc += 1
    elif int(r1) != 0:
      if r2.isalpha():
        pc += registers[r2]
      else:
        pc += int(r2)
    else:
      pc += 1
  #if i == 100:
  #  break
  #print(registers)

print(registers['h'])
