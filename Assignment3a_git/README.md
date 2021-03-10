# Assignment 3
### q1
 - The basic algorithm is to make chain of path from given empids to the topmost employee.
 - Then compare both chains till there is common element.The last common root is the answer.
 - Input empid is assumed to be present in the tree
 - It is assumed that there will be only one node in L0 and that will be the global root of employee hierarchy.

### q2
  - Calculate total number of days till each date from 1/1/1 and then find the difference of them.
  - Input file is assumed to have input like "Date1: 10th September, 2020" and NOT like "10th September, 2020"
  - It is assumed there will be spaces between date,month and year and Initcap format for name and abbreviation of month. Example "10th September, 2020" , "10th Sep, 2020".
  - Basically input is assumed to be formatted as given in examples in the assignment (even including the commas).
### q3
 -  Process both inputs to get time slots in minutes as a list of list.
 -  Append both lists  to a single list and sort it.
 -  Merge intervals so as to get the busy times.
 -  Using busy list find the free slot list.
 -  Input the time slot duration and find available slot in the free slot list.
 -  Assume atleast one interval will be given as input.
 -  It is assumed the starting and ending time in a slot will not be same
 -  It is assumed that the slots of a particular employee dont overlap among themselves.
### Github Link
