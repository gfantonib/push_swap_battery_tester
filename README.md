# push_swap_battery_test

![Animated GIF](https://media1.tenor.com/m/fSf2R4cpx1cAAAAd/surfs-up.gif)

## This tester orchestrates a competition among selected push_swap repositories. For each push_swap repository, it calculates the execution time and the number of movements.
```sh
git clone https://github.com/gfantonib/push_swap_battery_tester.git
cd push_swap_battery_tester
cd battery
python3 main.py
```
### To set up the race, follow these examples:

### Specify the repositories you want in the race with only one space between them:
**https://github.com/mcombeau/push_swap.git https://github.com/LeoFu9487/push_swap.git https://github.com/ayogun/push_swap.git**

### 2. Assign a name to each repository respectively:
**mia_combeau leo_fu yigit_ogun**

### 3. Determine the sets, i.e., the number of elements you want the program to execute. Each set will be filled with random numbers:
**3 5 100 500**

### 4. Specify how many times the program runs for each set of numbers. This indicates how many times ./push_swap {...} is going to be executed for each set. The average time and movements will be calculated:
**10**

