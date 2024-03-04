# push_swap_battery_test

<div align="center">
  <img src="https://media0.giphy.com/media/xTgeJ2osZDHtVjtGXC/giphy.gif?cid=ecf05e47qsgycy8ndsysxie9wyszu4w47tzajx34iie59qac&ep=v1_gifs_search&rid=giphy.gif&ct=g.gif" alt="Animated GIF">
</div>

## This tester orchestrates a competition among selected push_swap repositories.
### For each push_swap repository, it calculates the execution time and the number of movements.
### All you need is a repository with a Makefile that compiles a *push_swap* executable.
```sh
git clone https://github.com/gfantonib/push_swap_battery_tester.git
cd push_swap_battery_tester
cd battery
python3 main.py
```
### To set up the race (battery), follow these examples:

1. Specify the repositories you want in the race with only one space between them:\
**https://github.com/mcombeau/push_swap.git https://github.com/LeoFu9487/push_swap.git https://github.com/ayogun/push_swap.git**

2. Assign a name to each repository respectively:\
**mia_combeau leo_fu yigit_ogun**

3. Determine the sets, i.e., the number of elements you want the program to execute. Each set will be filled with random numbers:\
**3 5 100 500**

4. Specify how many times the program runs for each set of numbers.\
This indicates how many times ./push_swap {...} is going to be executed for each set.\
The average time and movements will be calculated:\
**10**

### If you want to use the ecxacly the same inputs and compare the results between the chosen repositories, use the battery_2.

