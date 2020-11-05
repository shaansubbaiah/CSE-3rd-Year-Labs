#! /bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# temp conversion

echo "Input temp in Celcius:"
read c

echo "scale=2; (9 / 5 * $c + 32)" | bc
