#!/bin/sh

# Get numbers interactively
if [ $# -eq 0 ]; then
    echo "Enter 2 numbers:"
    read a b
# Get numbers from arguments
else
    a=$1
    b=$2
fi

# Set m to the lowest number
if [ $a -lt $b ]; then
    m=$a
else
    m=$b
fi

while [ $m -ne 0 ]; do
    ad=$(expr $a % $m)
    bd=$(expr $b % $m)

    # If both are divisible, m is GCD
    if [ $ad -eq 0 -a $bd -eq 0 ]; then
        echo "GCD = " $m
        break
    fi

    # Decrement m
    m=$(expr $m - 1)
done
