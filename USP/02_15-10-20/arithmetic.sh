#! /bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# basic calculations

echo "
Menu:
    1.Add
    2.Sub
    3.Mul 
    4.Div
Choice:"
read ch

echo "Enter 2 values:"
read a b

case $ch in
1)
    echo "Sum: $(expr $a + $b)"
    ;;
2)
    echo "Sub: $(expr $a - $b)"
    ;;
3)
    echo "Mul: $(expr $a \* $b)"
    ;;
4)
    echo "Div: $(expr $a / $b)"
    ;;
*)
    echo "Invalid choice!"
    ;;
esac
