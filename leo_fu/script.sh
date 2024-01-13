#!/bin/bash

# Random numbers generation
shuf -i 0-10000 -n 1000 | tr '\n' ' ' > out0

# Run the push_swap command with timing information and redirect output to output.txt
(time ./push_swap $(<out0)) > out1 2>&1

# Use grep to extract the user time information and redirect it to output_2.txt
grep real out1 > out2

# Use awk to print the third column (user time) and redirect the result to a final output file
awk '{print $2}' out2 > out3

# Get number of moves
moves="$(cat out1 | wc -l)-4"
moves=$(echo $moves | bc -l)
echo $moves

# Get run time
time=$(cat out3)
echo $time
time=$(echo $time | cut -b 3,4,5,6,7)

# Make score
score=$(echo "1/$time*1/$moves" | bc -l)
echo $score

# Clean files
rm out0 out1 out2 out3