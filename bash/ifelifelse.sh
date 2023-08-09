#!/bin/bash

# when working with if else if statemements always remember to close it using fi at the end

# $1 is the first argument, the double commas (,,) converts the argument given into lower case making it caseinsensitive.
# [ 1 = 2 ] is the format of comparison in shell scripting.
# when running the script remember to pass in an argument.
# Don't forget to put the semicolons and then keyword

# example 
if [ ${1,,} = ven ]; then
    echo "hello ven"
elif [ ${1,,} = help ]; then
    echo "please entewr your user name"
else
    echo "I don't know you"
fi # this is a must

# echo $? - it returns the value of the exit command, 0 means True, 1 False