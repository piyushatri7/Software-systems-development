s = input().replace(" ","").lower()
list = {}
for c in s:
    list[c]=1

if len(list) == 26:
    print("YES")
else:
    print("NO")
