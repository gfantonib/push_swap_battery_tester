import subprocess
import time

# 3. Clone the repository and execute its Makefile
def clone_and_make(repository, repositorys_names, iter_rep):
	print(f"\n\n{repositorys_names[iter_rep].upper()}")
	command_1 = ["git", "clone", repository, repositorys_names[iter_rep]]
	command_2 = ["make", "-C", repositorys_names[iter_rep]]
	# print(command_1, command_2)
	subprocess.run(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run(command_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 7. Execute ./push_swap {numbers}
def exec_push_swap(repositorys_names, executable_name, numbers, iter_rep):
	command_1 = f"./{repositorys_names[iter_rep]}/{executable_name} {numbers}"
	time_start = time.time()
	output = subprocess.run(command_1, shell=True, check=True, stdout=subprocess.PIPE, text=True)
	time_end = time.time()
	time_elapsed = time_end - time_start
	return (output, time_elapsed)

# 9. Clean the mess
def clean_the_mess(repositorys_names, iter_rep):
		command_1 = ["rm", "-rf", repositorys_names[iter_rep]]
		subprocess.run(command_1)
