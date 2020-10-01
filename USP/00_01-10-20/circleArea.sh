#!/bin/sh

# Shaan Subbaiah B C - 1BM18CS096
# program to find area of a circle

echo -n "Radius: "
read radius

area=$(echo "3.14 * $radius * $radius" | bc)
echo "Area of circle = " $area " sq. units"
