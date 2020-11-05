#! /bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# find permutations for 1,2,3

for ((i = 1; i <= 3; i++)); do
    for ((j = 1; j <= 3; j++)); do
        for ((k = 1; k <= 3; k++)); do
            echo $i $j $k
        done
    done
done
