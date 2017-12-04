from sys import stdin

acc = 0

#part 1
for line in stdin:
  s = line.replace("\n","").split(" ")
  words = []
  valid = True
  for word in s:
    if word in words:
      valid = False
      break
    else:
      words.append(word)
  if valid:
    acc += 1
    print(acc)

#part 2
def is_anagram(s1,s2):
  return sorted(s1) == sorted(s2)

for line in stdin:
  s = line.replace("\n","").split(" ")
  words = []
  valid = True
  for word1 in s:
    for word2 in words:
      if is_anagram(word1,word2):
        valid = False
        break
    if not(valid):
      break
    words.append(word1)
  if valid:
    acc += 1
    print(acc)
