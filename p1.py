captcha = list(map(int,input().strip()))

acc = 0

for i in range(len(captcha)):
  if i != len(captcha)-1:
    if captcha[i] == captcha[i+1]:
      acc += captcha[i]
  else: #circular
    if captcha[i] == captcha[0]:
      acc += captcha[i]

print(acc)
