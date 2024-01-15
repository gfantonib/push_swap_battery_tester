from utils import execs
from utils import formats

# input
repositorys, repository_name, number_of_numbers, executable_name = formats.pick_inputs()

# run test for the three reps
rep_iteration = 0
for rep in repositorys:

	# git clone mia rep and make executable
	execs.clone_and_make(repositorys, repository_name, rep_iteration)
	
	# execute 10 times
	time_total = 0
	moves_total = 0
	iteration = 0

	while (iteration < 10):
		# random number generator
		numbers = formats.random_generator(number_of_numbers)

		# exec push_swap
		output, time_elapsed = execs.exec_push_swap(repository_name, executable_name, numbers, rep_iteration, iteration)
		time_total = time_total + time_elapsed

		# format moves
		moves = formats.format_moves(output)
		moves_total = moves_total + moves

		iteration = iteration + 1

	# clean the mess
	execs.clean_the_mess(repository_name, rep_iteration)

	# print moves and time
	formats.print_output(moves_total, time_total, iteration)
	
	rep_iteration = rep_iteration + 1