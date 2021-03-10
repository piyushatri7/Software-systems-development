list1 =  input().split(",")
#sally,Dylan,rebecca,Diana,Joanne,keith

sum = 0
#print(type(list1)) 

list1 = list( filter(lambda x : x[0].isupper(),list1))

print(list1)

for item in list1:
    sum += len(item)
print(sum)
print(list1)
