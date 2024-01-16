import random

# 1. Get input from user
def pick_inputs():
	print("\nPut the repositorys links that you want inside the competition with only one space between them.\n\
If you want to run only one repository, that is fine to.")
	input_1 = input()
	print("\nNow you need to name each one of those repositories, respectively.")
	input_2 = input()
	repositorys_links = input_1.split()
	repositorys_names = input_2.split()
	if (len(repositorys_names) != len(repositorys_links)):
		print("\nThe number of repositorys needs to be the same as the number of names!")
		exit()
	print("\nChoose how many times the program runs for each set of numbers.")
	input_3 = input()
	iter_max = int(input_3)
	list_amount_numbers = [3, 5, 100, 500]
	executable_name = "push_swap"
	return (repositorys_links, repositorys_names, list_amount_numbers, executable_name, iter_max)

# 6. Random number generator
def random_generator(amount_numbers):
	randomlist = []
	for i in range(0, amount_numbers):
		randomlist.append(i)
	random.shuffle(randomlist)
	numbers = ' '.join(map(str, randomlist))
	return (numbers)

# 8. Format moves
def format_moves(output):
	moves = output.stdout
	moves = moves.replace('\n', ' ')
	moves = len(moves.split())
	return (moves)