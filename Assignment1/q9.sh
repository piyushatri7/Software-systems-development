#!/bin/bash

read input_string

checksum=0
table=(0 2 4 6 8 1 3 5 7 9)		#double of every digit


input_string="$(echo "$input_string" | tr -d ' ')"	#delete spaces


if [[ "${#input_string}" -lt 2 ]] 	#check length <2
then
	echo  Invalid
	exit
	
else
	
	if [[ ${input_string} =~ ^[0-9]+$ ]] 	#check if contains any non-digits using regular expression
	then
		
		i=$((${#input_string} - 1))	#last index
		
		while [ "$i" -ge "0" ]
		do
			checksum="$(($checksum +  ${input_string:$i:1}))" 		#store last digit
			
			if [ $((i - 1)) -ge "0" ]
			then
				#echo $checksum
				checksum="$(($checksum + ${table[${input_string:$((i - 1)):1}]}))" 		#add every Second digit
				
			fi
			
			i=$((i - 2))
		done

		if [[ "$(($checksum % 10))" -eq "0" && "$checksum" -ne "0" ]]
		then
			echo Valid 
			#echo $checksum "$(($checksum % 10))"
			
		else
			echo Invalid
			#echo $checksum
		fi
		
	else	
		echo Invalid		#string contains non Digits
		exit
	fi
fi

