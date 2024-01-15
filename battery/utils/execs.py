import subprocess
import random
import time

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

# git clone mia rep and make executable
def clone_and_make(repositorys, repository_name, rep_iteration):
	print(repository_name[rep_iteration].upper())
	command_1 = ["git", "clone", repositorys[rep_iteration], repository_name[rep_iteration]]
	command_2 = ["make", "-C", repository_name[rep_iteration]]
	print(command_1, command_2)
	subprocess.run(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run(command_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# random number generator
def random_generator(number_of_numbers):
	randomlist = []
	for i in range(0, number_of_numbers):
		randomlist.append(i)
	random.shuffle(randomlist)
	numbers = ' '.join(map(str, randomlist))
	return (numbers)

# get the exec time of ./push_swap
def exec_push_swap(repository_name, executable_name, numbers, rep_iteration, iteration):
	command_1 = f"./{repository_name[rep_iteration]}/{executable_name} {numbers}"
	time_start = time.time()
	output = subprocess.run(command_1, shell=True, check=True, stdout=subprocess.PIPE, text=True)
	time_end = time.time()
	time_elapsed = time_end - time_start
	print(f"({iteration})\n   Time: {time_elapsed:.4f}s")
	return (output, time_elapsed)

# format moves
def format_moves (output):
	moves = output.stdout
	moves = moves.replace('\n', ' ')
	moves = len(moves.split())
	print(f"   Moves: {moves}")
	return (moves)

# clean the mess
def clean_the_mess (repository_name, rep_iteration):
		command_1 = ["rm", "-rf", repository_name[rep_iteration]]
		subprocess.run(command_1)

# print moves and time
def print_output (moves_total, time_total, iteration):
	print(50 * "-")
	print(f"Moves mean: {moves_total / iteration} | Moves total: {moves_total}")
	print(f"Time mean: {time_total / iteration:.4f}s | Time total: {time_total:.4f}s")
	print(50 * "-")
	print("\n")
