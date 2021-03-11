#!/bin/bash

val=$1
for (( i=2 ; i<=$# ; i++ ));		# $# for number of args
do
        x=${!i} 			#select ith arg
        val=$(bc <<< "$val^$x")  
        
        #echo $x	
done
echo $val;
