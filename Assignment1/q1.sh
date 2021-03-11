#!/bin/bash

mkdir Assignmnet1
cd Assignmnet1

touch lab{1..5}.txt

#rename 's/.txt/.c/' *.txt

find . -name "*.txt" -exec bash -c 'file="{}"; mv -- "$file" "${file%.txt}.c"' \;

#find all .txt files and execute bash commands to rename them to .c
#-exec is execute
#bash -c is an Inline bash script	

ls -lSr

find /home  -maxdepth 2

find "$(pwd)" -name "*.txt"	#print full path using pwd and match filename using -name
