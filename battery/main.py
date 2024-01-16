from utils import execs
from utils import formats

# 1. Get input from user
repositorys_links, repositorys_names, list_amount_numbers, executable_name, iter_max = formats.pick_inputs()

# 2. Iterate program for several repositorys
iter_rep = 0
for repository in repositorys_links:
	# 3. Clone the repository and execute its Makefile
	execs.clone_and_make(repository, repositorys_names, iter_rep)
	# 4. Iterate for the sets (3, 5, 100, 500)
	for amount_numbers in list_amount_numbers:
		# 5. Iterete, for each set, iter_max times 
		time_total = 0
		moves_total = 0
		iter_exec = 0
		while (iter_exec < iter_max):
			# 6. Random number generator
			numbers = formats.random_generator(amount_numbers)
			# 7. Execute ./push_swap {numbers}
			output, time_elapsed = execs.exec_push_swap(repositorys_names, executable_name, numbers, iter_rep)
			time_total = time_total + time_elapsed
			# 8. Format moves
			moves = formats.format_moves(output)
			moves_total = moves_total + moves
			iter_exec = iter_exec + 1
		print(f"{amount_numbers} Numbers")
		print(f"Time mean: {time_total / iter_max:.4f}s | Moves mean: {moves_total / iter_max}\n")

	# 9. Clean the mess
	execs.clean_the_mess(repositorys_names, iter_rep)
	iter_rep = iter_rep + 1