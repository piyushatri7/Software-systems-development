#!/bin/bash

read input

len=${#input}

a=($(compgen -c | tr " " "\n"))	#store commands in array

input=$(echo $input | grep -o . | sort |tr -d " ")	#sort input

n=${#a[@]}

for((i=0;i<$n;i++))
{
	if [[ $len == ${#a[$i]} ]]			#length check
	then
		sorted=$(echo ${a[$i]} | grep -o . | sort |tr -d " ")	#sort each command and match with input
		if [[ $input == $sorted ]]
		then
			echo Yes
			echo ${a[$i]} 
			exit
		fi
	fi
}
echo No	#command not found
