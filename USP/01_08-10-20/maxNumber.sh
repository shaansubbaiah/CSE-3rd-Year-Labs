#! /bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# Max of 3 numbers

echo -n "Enter 3 numbers: "
read a b c

if [ $a -gt $b ]; then
    if [ $a -gt $c ]; then
        echo $a "is max."
    elif [ $c -gt $a]; then
        echo $c "is max."
    fi
else
    if [ $c -gt $b ]; then
        echo $c "is max."
    else
        echo $b "is max."
    fi
fi

# Using AND

# if [ $a -gt $b ]  && [ $a -gt $c ]; then
#     echo $a "is max."
# elif [ $c -gt $a]  && [ $c -gt $b ]; then
#     echo $c "is max."
# else
#     echo $b "is max."
# fi
