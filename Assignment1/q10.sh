#!/bin/bash

read op

if [[ $op == "*" ]]
then
	read n			#read num of operands
	read n1		#read first operand
	while [ $n != 1 ]
	do
		read n2
		#n1=$(($n1*$n2))
		n1=$(bc <<< "scale=10;$n1*$n2")
		n=$((n-1))
		n1=`printf "%.4f" $n1`
	done


###########################################################


elif [[ $op == "+" ]]
then
	read n			#read num of operands
	read n1		#read first operand
	while [ $n != 1 ]
	do
		read n2
		#n1=$(($n1+$n2))
		n1=$(bc <<< "scale=10;$n1+$n2")
		n=$((n-1))
		n1=`printf "%.4f" $n1`
	done


###########################################################

elif [[ $op == "-" ]]
then
	read n			#read num of operands
	read n1		#read first operand
	while [ $n != 1 ]
	do
		read n2
		#n1=$(($n1-$n2))
		n1=$(bc <<< "scale=10;$n1-$n2")
		n=$((n-1))
		n1=`printf "%.4f" $n1`
	done


###########################################################

elif [ $op == "/" ]
then
	read n			#read num of operands
	read n1		#read first operand
	while [ $n != 1 ]
	do
		read n2
		#n1=$(($n1/$n2))
		#bc <<< 'scale=2; n1/n2'
		n1=$(bc <<< "scale=10;$n1/$n2")	#scale in bc is larger than 4
							#so that rounding off is correct in printf
		n=$((n-1))
		n1=`printf "%.4f" $n1`
	done
fi

###########################################################



echo "$n1"

