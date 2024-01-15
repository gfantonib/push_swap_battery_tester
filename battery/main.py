from utils import execs
from utils import formats

# input
repositorys, repository_name, number_of_numbers, executable_name, iter_max = formats.pick_inputs()

# run test for the three reps
rep_iteration = 0
for rep in repositorys:
	# git clone mia rep and make executable
	execs.clone_and_make(repositorys, repository_name, rep_iteration)

	for number in number_of_numbers:
		# execute 10 times
		time_total = 0
		moves_total = 0
		iteration = 0
		while (iteration < iter_max):
			# random number generator
			numbers = formats.random_generator(number)
			# exec push_swap
			output, time_elapsed = execs.exec_push_swap(repository_name, executable_name, numbers, rep_iteration, iteration)
			time_total = time_total + time_elapsed
			# format moves
			moves = formats.format_moves(output)
			moves_total = moves_total + moves
			iteration = iteration + 1
		print(f"{number} Numbers")
		print(f"Time mean: {time_total / iter_max:.4f}s | Moves mean: {moves_total / iter_max}\n")

	# clean the mess
	execs.clean_the_mess(repository_name, rep_iteration)
	# print moves and time
	# formats.print_output(moves_total, time_total, iteration)
	rep_iteration = rep_iteration + 1