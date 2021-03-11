#!/bin/bash

read str
str=$(echo "$str" | tr '[:upper:]' '[:lower:]')		#convert to lower case	
#echo $str

len=${#str}
len=`expr $len - 1`

#echo $len

i=0
while [ $i -le $len ]
do
	c1="${str:$i:1}"
	c2="${str:$len:1}"
	
	#c1=`echo $str | cut -c $i`		#-c option to get specific char
	#c2=`echo $str | cut -c $len`
	
	#echo "$c1  $c2"
	
	if [ $c1 != $c2 ]		#if any char not matched
	then
		echo "No"
		exit		
	fi
	
	i=`expr $i + 1`
	len=`expr $len - 1`
done

echo "Yes"
