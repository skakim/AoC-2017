m = []
for _ in range(201):
  l = list(input())
  m.append(l)

direction = 'd' #up,down,left,right
x = m[0].index("|")
y = 0
current = "|"
letters = []
i = 0
while(current != ' '):
  i += 1
  if direction == 'u':
    y -= 1
  elif direction == 'd':
    y += 1
  elif direction == 'l':
    x -= 1
  elif direction == 'r':
    x += 1
  current = m[y][x]
  if current.isalpha():
    letters.append(current)
  if current == '+':
    if direction == 'u' or direction == 'd':
      if m[y][x-1] != ' ':
        direction = 'l'
      else:
        direction = 'r'
    elif direction == 'l' or direction == 'r':
      if m[y-1][x] != ' ':
        direction = 'u'
      else:
        direction = 'd'
  if i % 1000 == 0:
    print(i)

print("".join(letters))
print(i)
