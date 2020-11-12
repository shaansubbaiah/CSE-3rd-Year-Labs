echo -n "Enter a string: "
read str

echo "$str" | grep -o "[aeiouAEIOU]" | wc -l
