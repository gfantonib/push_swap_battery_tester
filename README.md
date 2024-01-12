### Random generator
```sh
shuf -r -i 0-1 -n 100 | tr '\n' ' '
```
### Time and Moves
```sh
time ./push_swap $(<random_1) && ./push_swap $(<random_1) | wc -l
```
### Redirect time and ./push_swap output to file
(time ./push_swap $(<random_1)) > output.txt 2>&1

### 
(time ./push_swap $(<random_1)) > output.txt 2>&1 && grep user output.txt > output_2.txt && awk '{print $3}' output_2.txt

## References
### Jamie Dawson
https://github.com/JamieDawson/push_swap_final

### Leo Fu
https://github.com/LeoFu9487/push_swap

### Mia Combeau
https://github.com/mcombeau/push_swap

### A. Yigit Ogun
https://github.com/ayogun/push_swap?tab=readme-ov-file
