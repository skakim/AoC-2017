tape = {0:0}
states = {}
states['A'] = [(1,1,'B'),(0,1,'C')]
states['B'] = [(0,-1,'A'),(0,1,'D')]
states['C'] = [(1,1,'D'),(1,1,'A')]
states['D'] = [(1,-1,'E'),(0,-1,'D')]
states['E'] = [(1,1,'F'),(1,-1,'B')]
states['F'] = [(1,1,'A'),(1,1,'E')]
cursor = 0
state = 'A'

for i in range(12368930):
  if i % 100000 == 0:
    print(i, len(tape.keys()), cursor, state)
  if cursor not in tape.keys():
    tape[cursor] = 0
  action = states[state][tape[cursor]]
  tape[cursor] = action[0]
  cursor += action[1]
  state = action[2]

acc = 0
for k in tape.keys():
  acc += tape[k]
print(acc)
