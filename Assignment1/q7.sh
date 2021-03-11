#!/bin/bash

read n

(ps -au| awk '{print $2;}' | sort -n| sed '1d') > pid.txt;

lines=$(head -${n} pid.txt)		#store n lines in variable to remove first newline

echo $lines | tr ' ' '\n'		#replace spaces with \n to restore
