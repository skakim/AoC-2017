#part 1
A = int(input().split(" ")[-1])
B = int(input().split(" ")[-1])

score = 0
for i in range(40000000):
  A = (A*16807)%2147483647
  B = (B*48271)%2147483647
  if bin(A)[-16:] == bin(B)[-16:]:
    score += 1
  if i % 1000000 == 0:
    print(i)

print(score)

#part 2
A = int(input().split(" ")[-1])
B = int(input().split(" ")[-1])

score = 0
counter = 0
numbers_A = []
numbers_B = []
while True:
  A = (A*16807)%2147483647
  while A % 4 != 0:
    A = (A*16807)%2147483647
  B = (B*48271)%2147483647
  while B % 8 != 0:
    B = (B*48271)%2147483647
  counter += 1
  if bin(A)[-16:] == bin(B)[-16:]:
    score += 1
  if counter % 100000 == 0:
    print(counter)
  if counter == 5000000:
    break
print(score)
