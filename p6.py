banks = list(map(int,input().split("\t")))

#part 1
seen = []
acc1 = 0
while tuple(banks) not in seen:
  acc1 += 1
  seen.append(tuple(banks))
  i = banks.index(max(banks))
  temp = banks[i]
  banks[i] = 0
  i = (i+1)%(len(banks))
  while(temp != 0):
    banks[i] += 1
    temp -= 1
    i = (i+1)%(len(banks))
print(acc1)

#part 2 (could have been only "print len(seen) - seen.index(tuple(banks))" =( )
already_seen=tuple(banks)
new = []
acc2 = 0
while tuple(new) != already_seen:
  acc2 += 1
  i = banks.index(max(banks))
  temp = banks[i]
  banks[i] = 0
  i = (i+1)%(len(banks))
  while(temp != 0):
    banks[i] += 1
    temp -= 1
    i = (i+1)%(len(banks))
  new = banks
print(acc2)
