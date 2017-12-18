import string

program = []
for _ in range(41):
  program.append(input().split(" "))

#part2 only

class Instance:
  def __init__(self, prog, id):
    self.program = prog
    self.last_sound = -1
    self.pc = 0
    self.registers = {x:0 for x in string.ascii_lowercase}
    self.registers['p'] = id
    self.waiting = False
    self.queue = []
    
  def step(self):
    instr = self.program[self.pc][0]
    if instr == 'set':
      r1 = self.program[self.pc][1]
      r2 = self.program[self.pc][2]
      if r2.isalpha():
        self.registers[r1] = self.registers[r2]
      else:
        self.registers[r1] = int(r2)
      self.pc += 1
    elif instr == 'add':
      r1 = self.program[self.pc][1]
      r2 = self.program[self.pc][2]
      if r2.isalpha():
        self.registers[r1] += self.registers[r2]
      else:
        self.registers[r1] += int(r2)
      self.pc += 1
    elif instr == 'mul':
      r1 = self.program[self.pc][1]
      r2 = self.program[self.pc][2]
      if r2.isalpha():
        self.registers[r1] *= self.registers[r2]
      else:
        self.registers[r1] *= int(r2)
      self.pc += 1
    elif instr == 'mod':
      r1 = self.program[self.pc][1]
      r2 = self.program[self.pc][2]
      if r2.isalpha():
        self.registers[r1] %= self.registers[r2]
      else:
        self.registers[r1] %= int(r2)
      self.pc += 1
    elif instr == 'snd':
      r1 = self.program[self.pc][1]
      if r1.isalpha():
        self.last_sound = self.registers[r1]
        self.pc += 1
        return self.last_sound
      else:
        self.last_sound = int(r1)
        self.pc += 1
        return self.last_sound
      self.pc += 1
    elif instr == 'rcv':
      r1 = self.program[self.pc][1]
      if len(self.queue) > 0:
        self.registers[r1] = self.queue.pop(0) #30 min until I realize I was doing "pop()"
        self.pc += 1
        self.waiting = False
      else:
        self.waiting = True
    elif instr == 'jgz':
      r1 = self.program[self.pc][1]
      r2 = self.program[self.pc][2]
      if (r1.isalpha()):
        if self.registers[r1] > 0:
          if r2.isalpha():
            self.pc += self.registers[r2]
          else:
            self.pc += int(r2)
        else:
          self.pc += 1
      elif int(r1) > 0:
        if r2.isalpha():
          self.pc += self.registers[r2]
        else:
          self.pc += int(r2)
      else:
        self.pc += 1
    return 'ok'

p0 = Instance(program, 0)
p1 = Instance(program, 1)
counter = 0
i = 0
while(not(p0.waiting and p1.waiting)):
  op = p0.step()
  if op != 'ok':
    p1.queue.append(op)
  op = p1.step()
  if op != 'ok':
    p0.queue.append(op)
    counter += 1
  i += 1
  if i % 100000 == 0:
    print(p0.pc, p1.pc, counter)
print(counter)
