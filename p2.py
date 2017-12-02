acc1 = 0
acc2 = 0

for _ in range(16):
  line = list(map(int,input().split("\t")))
  acc1 += max(line)-min(line)
  
  for i in line:
    for j in line:
      if (i == j): 
        continue
      if i % j == 0:
        acc2 += i/j

print(acc1,acc2)
