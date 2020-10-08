#! /bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# check if num is +ve, -ve, 0

echo -n "Enter a number: "
read num

if [ $num -gt 0 ]; then
    echo "+ve"
elif [ $num -lt 0 ]; then
    echo "-ve"
else
    echo "0"
fi
