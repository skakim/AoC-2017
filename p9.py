s = input()

#filter and part 2
filtered = ""
garbage_mode = False
i = 0
garbage_count = 0
while i < len(s):
  if s[i] == '!':
    i += 1
  elif s[i] == "<" and not(garbage_mode):
    garbage_mode = True
  elif garbage_mode and s[i] == ">":
    garbage_mode = False
  elif garbage_mode:
    garbage_count += 1
  elif not(garbage_mode):
    filtered += s[i]
  i += 1

#part 1
deep = 1
score = 0
for c in filtered:
  if c == '{':
    score += deep
    deep += 1
  elif c == '}':
    deep -= 1

#part 1
print(score)
#part 2
print(garbage_count)
