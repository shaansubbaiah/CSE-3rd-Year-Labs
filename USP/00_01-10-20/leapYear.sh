#!/bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# program to check for a leap year

echo -n "Year: "
read year

is_leap=0

if [ $(expr $year % 4) = 0 ]; then
    if [ $(expr $year % 100) = 0 ] && [ $(expr $year % 400) = 1 ]; then
        is_leap=1
    else
        is_leap=0
    fi
    is_leap=1
else
    is_leap=0
fi

if [ $is_leap = 1 ]; then
    echo $year "is a Leap Year."
else
    echo $year "is not a Leap Year."
fi
