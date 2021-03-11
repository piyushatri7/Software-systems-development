#!/bin/bash

HISTFILE=~/.bash_history
set -o history			#enable hstory command

history 10 | awk '{print $2}' > hist2.txt

cat hist2.txt | awk '{count[$1]++} END{for (i in count) print count[i] , i}'	 | sort -rn | awk '{print $2 , $1}'	
		#store in count array	and print the count and command            
