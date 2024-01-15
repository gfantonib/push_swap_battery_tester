import random

# input
def pick_inputs():
	print("Put the repositorys links that you want inside the competition with only one space between them.\n\
	If you want to run only one repository, that is fine to.")
	input_1 = input()
	print("Now you need to name each one of those repositories, respectively.")
	input_2 = input()
	repositorys = input_1.split()
	repository_name = input_2.split()
	if (len(repository_name) != len(repositorys)):
		print("The number of repositorys needs to be the same as the number of names!")
		exit()
	print("Choose the amount of numbers that goes as parameters of your ./push_swap")
	input_3 = input()
	number_of_numbers = int(input_3)
	executable_name = "push_swap"
	return (repositorys, repository_name, number_of_numbers, executable_name)

# random number generator
def random_generator(number_of_numbers):
	randomlist = []
	for i in range(0, number_of_numbers):
		randomlist.append(i)
	random.shuffle(randomlist)
	numbers = ' '.join(map(str, randomlist))
	return (numbers)

# format moves
def format_moves (output):
	moves = output.stdout
	moves = moves.replace('\n', ' ')
	moves = len(moves.split())
	print(f"   Moves: {moves}")
	return (moves)

# print moves and time
def print_output (moves_total, time_total, iteration):
	print(50 * "-")
	print(f"Moves mean: {moves_total / iteration} | Moves total: {moves_total}")
	print(f"Time mean: {time_total / iteration:.4f}s | Time total: {time_total:.4f}s")
	print(50 * "-")
	print("\n")