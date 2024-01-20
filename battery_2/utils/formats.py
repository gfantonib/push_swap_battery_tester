import random

# 1. Get input from user
def pick_inputs():
	print(
"\n1. Put the repositorys links that you want inside the competition with only one space between them.\
\nIf you want to run only one repository, that is fine to.\
\nExemple:\
\nhttps://github.com/mcombeau/push_swap.git https://github.com/LeoFu9487/push_swap.git https://github.com/ayogun/push_swap.git")
	input_1 = input()
	print(
"\n2. Now you need to name each one of those repositories, respectively.\
\nExemple:\
\nmia_combeau leo_fu yigit_ogun")
	input_2 = input()
	repositorys_links = input_1.split()
	repositorys_names = input_2.split()
	if (len(repositorys_names) != len(repositorys_links)):
		print(
"\nThe number of repositorys needs to be the same as the number of names!")
		exit()
	print(
"\n3. Chose the sets (the amount of numbers) that you want the program to execute.\
\nExemple:\
\n3 5 100 500")
	input_3 = input()
	input_3 = input_3.split()
	list_amount_numbers = [int(x) for x in input_3]
# 	print(
# "\n4. Choose how many times the program runs for each set of numbers.\
# \nThe average time and movements will be calculated.\
# \nExemple:\
# \n10")
# 	input_4 = input()
# 	iter_max = int(input_4)
	executable_name = "push_swap"
	return (repositorys_links, repositorys_names, list_amount_numbers, executable_name)

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