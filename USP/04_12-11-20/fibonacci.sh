echo "Series length:"
read n

a=0
b=1
tmp=0

for ((i = 1; i <= n; i++)); do
    tmp=$a
    a=$(expr $a + $b)
    echo -n " $a"
    b=$tmp
done
