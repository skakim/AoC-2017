def get_chars(start, end):
    return ''.join(chr(c) for c in range(ord(start), ord(end)+1))
    
program = []
for _ in range(32):
  program.append(input().split(" "))

registers = {x:0 for x in get_chars('a','h')}
pc = 0
i = 0
counter = 0
#part 1
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
    counter += 1
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
print(counter)

#part2 -> my version of the assembly code in Python
a,b,c,d,e,f,g,h = [1] + [0]*7
b = 67
c = b
if a != 0:
  b = b*100 + 100000
  c = b + 17000
first_time = True #emulate "do while"
while(first_time or g!=0):
  first_time = False
  f = 1
  d = 2
  e = 2
  while (d*d < b): #checking if b is prime
    if (b%d) == 0: #in the code, it does g = d*e == b, doing for(d){for(e)} in an really inneficient way
      f = 0 #flag "is_prime" -> false
    d += 1
  if f == 0: #if is not prime
    h += 1
  g = b-c #therefore, it is "while b != c"
  b += 17 #difference = 17000, then 1000 iterations
print(h) #h = how much NOT prime numbers are in range(106700,123717,17)
