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
    
"""
print parent dictionary    
for root in parent:
    print(root,parent[root])
print()
print level dictionary    
for root in level:
    print(root,level[root])
"""
inp = input().split()

empcount = int(inp[0])
empidlist= []
flag = 0
for i in range(1,empcount+1):
    empid = inp[i]            
    if empid == globalroot:     #no leader exists condition
        flag = 1
    empidlist.append(empid)

#no common leader found
if flag == 1:
    print("Leader not found")
    
else:
    chains = []
    for empid in empidlist:
        #create empid to root path
        parentchain = [empid]
        temp = empid
        while temp != globalroot :
            parentchain.append(parent[temp])
            temp = parent[temp]

        #reverse to get root to empid1 path
        parentchain.reverse()
        chains.append(parentchain)
    #print(chains)
    

    chainlen = []
    for chain in chains:
        chainlen.append(len(chain))
    #print(chainlen)

    commlead = globalroot
    
    i=0
    #traverse smllest chain               
    while i < min(chainlen)-1 :  #case when one empid is in chain of other
        brkflag = 0
        for chain in chains:        #check if ith element in all chains is equal
            if chain[i] != chains[0][i]:
                brkflag = 1

        if brkflag == 1:
            break
        
        commlead = chains[0][i]
        i += 1
        
    print("common leader: " + str(commlead))

    for empid in empidlist:    
        print("leader " + str(commlead) +" is " + str(abs(level[commlead] - level[empid])) + " levels above employee " + str(empid))
    
