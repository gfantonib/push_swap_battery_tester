import subprocess
import random
import time

time_total = 0
moves_total = 0
iteration = 0

while (iteration < 10):
	# Random number generator
	randomlist = []
	for i in range(0, 1000):
		randomlist.append(i)
	random.shuffle(randomlist)
	numbers = ' '.join(map(str, randomlist))

	# Get the exec time of ./push_swap
	command = f"./push_swap {numbers}"
	time_start = time.time()
	moves_and_time = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)
	time_end = time.time()
	time_elapsed = time_end - time_start
	print(f"({iteration}) time: {time_elapsed}")
	time_total = time_total + time_elapsed

	# format moves
	moves = moves_and_time.stdout
	moves = moves.replace('\n', ' ')
	moves = len(moves.split())
	print(f"moves: {moves}")
	moves_total = moves_total + moves

	iteration = iteration + 1

# print moves and time
print(50 * "-")
print(f"Moves mean: {moves_total / iteration} | Moves total {moves_total}")
print(f"Time mean: {time_total / iteration} | time total {time_total}")