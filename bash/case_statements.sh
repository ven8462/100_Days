#!/bin/bash

# case statetements are mostly used to check for multiple values
# it is very easy to read
# case statements perform different actions depending on which case is true
# case statements are similar to switch statements in C.
# The case statement starts with the case keyword followed by the $variable and the in keyword.
#The statement ends with the esac keyword, which is case spelled backward.The script compares the input $variable against the patterns in each clause until it finds a match.
#A pattern and its commands make a clause, which ends with ;;.
#The script executes the commands corresponding to the first pattern matching the input $variable.
#The asterisk * symbol defines the default case, usually in the final pattern

# example

echo "Enter number"
read num
case $num in 
1)
echo "number 1";;
2)
echo "number 2";;
3)
echo "number 3";;
4)
echo "number 4";;
*)
echo "can only enter 1 to 4"
esac