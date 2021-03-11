# Assignment 1

### Q1
  - Use of basic commands for all the tasks.
  - Problem: Need to Install `rename` in ubuntu for this : `sudo apt install rename`[SOLVED]
  - Renamed .txt to .c files using `mv`.
  - Used `maxdepth` for search upto 2 level
  - [NOTE]No output will be printed for (f) part as there are no .txt files.
  
### Q2
  - [NOTE]This script will check if input can be ordered in any way to make a valid command. So the commands that are anagrams are assumed to be interchangable. The output will only be yes when input is valid command but doesn't take into account that the input is a valid command or not. For example :
  input=>cat
  output=>Yes tac 
  - Store all commands in an array.
  - Sort the input string lexicographically.
  - Iterate over command array, if length of command is equal to length of input then sort the command and compare with input. If matched then print the command otherwise continue.
  - Print No if no command matches.
  
##### [SCRAPPED METHOD]
- Gerate all permutations of input.
- Execute all permutations as command and send output to `/dev/null` so that there is no output.
- If command executed successfuly print "Yes" otherwise "No"
 - This method took long time for commands longer than 6 characters that is why it is scrapped.
 
### Q3
- Enable `history` command using `set -o history`
- Using `.bash_history` for history.
- Take last 10 commands and store in count array and print command and value for traversing.
- Sort in descending order based on count of command.

### Q4
- Retain everyting except number and separate them with single space.
- Problem: Leading and  trailing space still there[SOLVED]
- Remove leading and trailing space using `sed`.

### Q5
- Convert input to lower case using `tr`.
- Simple two  pointer approach. Put one pointer at start and one at end and compare them using loop. Then increment start pointer and decrement end pointer till (start < end).

### Q6
- Simple loop through arguments and exponentiate one by one.
- Used `bc` for computing larger values

### Q7
- Used `ps -au` for process ID.
- Problem: There is a newline in pid file at the beginning, might cause formatting issues[SOLVED].
- Used `awk`,`sort`,`sed` and `head` for formatting output.

### Q8
 - The script runs the `crontab` command and checks if correctly run or not.
 - Suppressed output using `/dev/null`.
 
### Q9
- Created table array to store doubled value of each number (also digits are added if required).
- Check if input contains any non-digits using regular expression.
- Applied Luhn's algorithm to calculate checksum.
- Check for checksum not equal to 0 and is divisible by 10 and print accordingly.

### Q10
- Read operator and execute accordingly using  `if else`.
- Use Loop for taking input and operating on each value.
- `bc` handles overflow.
- Problem in rounding off-   expected:0.6667  actual: 0.6666[SOLVED]
- Used `scale` for particular digit output and `printf` for rounding off.

