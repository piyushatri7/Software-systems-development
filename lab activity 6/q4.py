nums = input()
list = []
list = nums.split(",")
op = ""
flags = {}
for item in list:
    if item=="0000" or item=="1010" or item=="0101" or item=="1111":    #4 cases of 4 digit number divisible by 5
        flags[item]=item;

for x in flags:
    op = op + x + ","

print(op[:len(op)-1:1])     #remove last ,
        
