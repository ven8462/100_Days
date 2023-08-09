#!/bin/bash

# to create arrays in the terminal MY_ARRAY=(5 6 2 9 6)
# to display it echo $MY_ARRAY - this only displays the 1st index
# to display everything use echo ${MY_ARRAY[@]}
#@ is used as a place holder for index in scripting, you can specify the index you want ie 
# echo ${MY_ARRAY[3]} prints out value at index 3
# (#) the # can be used to get the length of a string eg echo string="hello"
# echo ${#string} - this gives you num of characters in the string

MY_LIST=(2 4 6 8 5)

#echo  ${MY_LIST[@]}

#for ((i=0; i <${#MY_LIST[@]}; i++)) # when used in this context # is used to get the length or number of items in the list.
#do
  #  echo " printing ${array[$i]}"
#done

for items in $MY_LIST; do echo 