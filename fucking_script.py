import subprocess
import random
import time

# chose rep and rep name
rep_1 = "https://github.com/mcombeau/push_swap.git"
rep_2 = "https://github.com/LeoFu9487/push_swap.git"
rep_3 = "https://github.com/ayogun/push_swap.git"

rep_1_name = "mia_combeau"
rep_2_name = "leo_fu"
rep_3_name = "yigit_ogun"

repositorys = [rep_1, rep_2, rep_3]
repository_name = [rep_1_name, rep_2_name, rep_3_name]
executable_name = "push_swap"
number_of_numbers = 10

# run test for the three reps
rep_iteration = 0
for rep in repositorys:

	# git clone mia rep and make executable
	print(repository_name[rep_iteration].upper())
	command_1 = ["git", "clone", repositorys[rep_iteration], repository_name[rep_iteration],]
	command_2 = ["make", "-C", repository_name[rep_iteration]]
	print(command_1, command_2)
	subprocess.run(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run(command_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# execute 10 times
	time_total = 0
	moves_total = 0
	iteration = 0

	while (iteration < 10):
		# random number generator
		randomlist = []
		for i in range(0, number_of_numbers):
			randomlist.append(i)
		random.shuffle(randomlist)
		numbers = ' '.join(map(str, randomlist))

		# get the exec time of ./push_swap
		command_1 = f"./{repository_name[rep_iteration]}/{executable_name} {numbers}"
		time_start = time.time()
		moves_and_time = subprocess.run(command_1, shell=True, check=True, stdout=subprocess.PIPE, text=True)
		time_end = time.time()
		time_elapsed = time_end - time_start
		print(f"({iteration})\n   Time: {time_elapsed:.4f}s")
		time_total = time_total + time_elapsed

		# format moves
		moves = moves_and_time.stdout
		moves = moves.replace('\n', ' ')
		moves = len(moves.split())
		print(f"   Moves: {moves}")
		moves_total = moves_total + moves

		iteration = iteration + 1

	# clean the mess
	command_1 = ["rm", "-rf", repository_name[rep_iteration]]
	subprocess.run(command_1)

	# print moves and time
	print(50 * "-")
	print(f"Moves mean: {moves_total / iteration} | Moves total: {moves_total}")
	print(f"Time mean: {time_total / iteration:.4f}s | Time total: {time_total:.4f}s")
	print(50 * "-")
	print("\n")

	rep_iteration = rep_iteration + 1