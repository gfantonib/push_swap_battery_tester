import subprocess
import random

# Random number generator
randomlist = []
for i in range(0, 2000):
	randomlist.append(i)
random.shuffle(randomlist)
numbers = ' '.join(map(str, randomlist))

# Get the exec time of ./push_swap
command = f"(time ./push_swap {numbers})"
moves_and_time = subprocess.run(
command, \
shell=True, \
check=True, \
stdout=subprocess.PIPE, \
stderr=subprocess.PIPE, \
text=True)

# Format moves
print("Moves output:")
moves = moves_and_time.stdout
moves = moves.replace('\n', ' ')
moves = len(moves.split())
print(moves)

# Format time
print("Time output:")
time = moves_and_time.stderr
time = time.split()
time = time[2]
time = time[0:7]
print(time)

