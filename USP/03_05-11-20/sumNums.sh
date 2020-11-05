#! /bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# sum of numbers

echo "Input upper limit:"
read max

sum=0

for ((i = 0; i < max; i++)); do
    sum=$(expr $sum + $i)
done

echo $sum
