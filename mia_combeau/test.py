import subprocess
import random

# Random number generator
randomlist = []
for i in range(0,10):
	randomlist.append(i)
random.shuffle(randomlist)
numbers = ' '.join(map(str, randomlist))

# Get the exec time of ./push_swap
command = f"./push_swap {numbers}"
moves = subprocess.run(
command, \
shell=True, \
check=True, \
stdout=subprocess.PIPE, \
stderr=subprocess.PIPE, \
text=True)

print("Command Output:")
print(moves.stdout)

print("Errors:")
print(moves.stderr)

