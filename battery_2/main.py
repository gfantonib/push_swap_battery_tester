from utils import execs
from utils import formats

# 1. Get input from user
repositorys_links, repositorys_names, list_amount_numbers, executable_name = formats.pick_inputs()

# 4. Iterate for the sets (3, 5, 100, 500)
for amount_numbers in list_amount_numbers:
	# 6. Random number generator
	numbers = formats.random_generator(amount_numbers)
	# 2. Iterate program for several repositorys
	iter_rep = 0
	print(f"\n\n{amount_numbers} NUMBERS:\n")
	for repository in repositorys_links:
		# 3. Clone the repository and execute its Makefile
		execs.clone_and_make(repository, repositorys_names, iter_rep)
		# 7. Execute ./push_swap {numbers}
		output, time_elapsed = execs.exec_push_swap(repositorys_names, executable_name, numbers, iter_rep)
		# 8. Format moves
		moves = formats.format_moves(output)
		print(f"{repositorys_names[iter_rep]}")
		print(f"Time: {time_elapsed:.4f}s | Move: {moves}\n")
		iter_rep = iter_rep + 1

	# 9. Clean the mess
	execs.clean_the_mess(repositorys_names)