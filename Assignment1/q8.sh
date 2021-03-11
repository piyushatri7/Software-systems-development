#!/bin/bash

if  crontab $1 > /dev/null 2>/dev/null	#check and suppress output of output stream and error stream
then
	echo "Yes"
else
	echo "No"
fi
