#!/bin/bash

read s

a="$(echo $s | tr '(' ' ' | tr ')' ' '  | tr -s ' ')"

a=$(echo "$a" | sed 's/^[ ]*//;s/[ ]*$//')		#substitute start end end space with nothing

echo "($a)" 

