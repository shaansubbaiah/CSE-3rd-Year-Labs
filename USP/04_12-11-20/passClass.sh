echo -n "Enter marks in 3 subjects: "
read m1 m2 m3

tot=$(expr $m1 + $m2 + $m3)
echo "Total: $tot"

per=$(expr $tot / 3)
echo "Percentage: $per"

if [[ $per -ge 90 ]]; then
    echo "S Grade"
elif [[ $per -ge 75 ]]; then
    echo "A Grade"
elif [[ $per -ge 60 ]]; then
    echo "B Grade"
elif [[ $per -ge 50 ]]; then
    echo "C Grade"
else
    echo "Fail"
fi
