import sys

def pat(p,v,a,t): #position_after_time
  return (v*t) + (1/2)*a*(t**2)

def distance(pos):
  d = 0.0
  for i in pos:
    d += abs(i)
  return d

particles_info = []
for _ in range(1000):
  particles_info.append((input().split(", ")))

print(particles_info[0])

min_distance = float(sys.maxsize)
min_particle = -1

i = 0
init_positions = []
init_vels = []
accs = []
for particle in particles_info:
  init_pos = list(map(int,particle[0][3:-1].split(",")))
  init_vel = list(map(int,particle[1][3:-1].split(",")))
  acc = list(map(int,particle[2][3:-1].split(",")))
  final_pos = [pat(init_pos[0],init_vel[0],acc[0],10000.0),pat(init_pos[1],init_vel[1],acc[1],10000.0),pat(init_pos[2],init_vel[2],acc[2],10000.0)]
  d = distance(final_pos)
  if d < min_distance:
    min_distance = d
    min_particle = i
  init_positions.append(init_pos)
  init_vels.append(init_vel)
  accs.append(acc)
  i += 1
print(min_particle, min_distance)

#part2
curr_pos = []
curr_vels = []
curr_accs = []
num_particles = 0
last_particles = 0
for i in range(1000):
  if init_positions[i] not in curr_pos:
    num_particles += 1
    curr_pos.append(init_positions[i])
    curr_vels.append(init_vels[i])
    curr_accs.append(accs[i])
  else:
    j = curr_pos.index(init_positions[i])
    num_particles -= 1
    del curr_pos[j]
    del curr_vels[j]
while True:
  seen_pos = []
  next_pos = []
  next_vels = []
  next_accs = []
  for i in range(len(curr_pos)):
    new_vel = [sum(x) for x in zip(curr_vels[i], curr_accs[i])]
    new_pos = [sum(x) for x in zip(curr_pos[i], new_vel)]
    if new_pos not in seen_pos:
      seen_pos.append(new_pos)
      next_pos.append(new_pos)
      next_vels.append(new_vel)
      next_accs.append(curr_accs[i])
    elif new_pos in next_pos:
      j = next_pos.index(new_pos)
      del next_pos[j]
      del next_vels[j]
      del next_accs[j]
      num_particles -= 2
    else:
      num_particles -= 1
  curr_pos = next_pos
  curr_vels = next_vels
  curr_accs = next_accs
  if last_particles != num_particles:
    print(num_particles)
  last_particles = num_particles
