import subprocess
import random
import time

# chose rep and rep name
repository = "https://github.com/mcombeau/push_swap.git"
repository_name = "mia_combeau"
executable_name = "push_swap"

# git clone mia rep and make executable
command_1 = ["git", "clone", repository, repository_name,]
command_2 = ["make", "-C", repository_name]
print(command_1, command_2)
subprocess.run(command_1)
subprocess.run(command_2, stdout=subprocess.PIPE)

# execute 10 times
time_total = 0
moves_total = 0
iteration = 0

while (iteration < 10):
	# random number generator
	randomlist = []
	for i in range(0, 1000):
		randomlist.append(i)
	random.shuffle(randomlist)
	numbers = ' '.join(map(str, randomlist))

	# get the exec time of ./push_swap
	command_1 = [f"./{repository_name}/{executable_name} {numbers}"]
	time_start = time.time()
	moves_and_time = subprocess.run(command_1, shell=True, check=True, stdout=subprocess.PIPE, text=True)
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

# clean the mess
command_1 = ["rm", "-rf", repository_name]
subprocess.run(command_1)

# print moves and time
print(50 * "-")
print(f"Moves mean: {moves_total / iteration} | Moves total: {moves_total}")
print(f"Time mean: {time_total / iteration} | Time total: {time_total}")