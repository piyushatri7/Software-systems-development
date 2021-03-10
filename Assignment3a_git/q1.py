import json

f = open("org.json","r")

jsontree = eval(f.read().replace("\n",""))

#for item in jsontree:
#    print(type(item),type(jsontree[item]))
#     for val in jsontree[item]:
#        print(val)

#get topmost employee
globalroot = jsontree["L0"][0]["name"]
#print("globalroot-> " + str(globalroot))


#store root:root_parent
parent = {}
#store root:root_level
level = {}

lv = 0
for item1 in jsontree:
    for item2 in  jsontree[item1]:
        #print(item2)
        root = item2["name"]
        par=""
        if root != globalroot:        #root has no parent
            par = item2["parent"]
        parent[root] = par
        level[root] = lv
    lv += 1

#print parent dictionary    
#for root in parent:
#    print(root,parent[root])
#print()
#print level dictionary    
#for root in level:
#    print(root,level[root])


empid1 = input()
empid2 = input()

#no common leader found
if empid1 == globalroot or empid2 == globalroot:
    print("Leader not found")
    
else:
    #create empid1 to root path
    parentchain1 = [empid1]
    temp1 = empid1
    while temp1 != globalroot :
        parentchain1.append(parent[temp1])
        temp1 = parent[temp1]

    #reverse to get root to empid1 path
    parentchain1.reverse()
    #print(parentchain1)

    #create empid2 to root path
    parentchain2 = [empid2]
    temp2 = empid2
    while temp2 != globalroot :
        parentchain2.append(parent[temp2])
        temp2 = parent[temp2]

    #reverse to get root to empid2 path
    parentchain2.reverse()
    #print(parentchain2)

    commlead = parentchain1[0]
    n1 = len(parentchain1)
    n2 = len(parentchain2)
    i=0
    #  -traverse smller one  -till parents are same                 -case when one empid is in chain of other
    while i < min(n1,n2) and parentchain1[i] == parentchain2[i] and parentchain1[i] != empid1 and parentchain2[i] != empid2:
        commlead = parentchain1[i]
        i += 1
    print(commlead)
    print(abs(level[commlead] - level[empid1]))
    print(abs(level[commlead] - level[empid2]))
