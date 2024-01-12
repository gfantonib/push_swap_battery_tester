#!/bin/bash

# random
shuf -i 0-10000 -n 1000 | tr '\n' ' ' > out0
# Run the push_swap command with timing information and redirect output to output.txt
(time ./push_swap $(<out0)) > out1 2>&1

# Use grep to extract the user time information and redirect it to output_2.txt
grep real out1 > out2

# Use awk to print the third column (user time) and redirect the result to a final output file
awk '{print $2}' out2 > out3

# Show result
cat out3

# Clean files
rm out0 out1 out2 out3