captcha = list(map(int,input().strip()))
steps = len(captcha)//2

acc = 0

for i in range(len(captcha)):
  j = int((i+steps)%len(captcha))
  if captcha[i] == captcha[j]:
    acc += captcha[i]
    
print(acc)
