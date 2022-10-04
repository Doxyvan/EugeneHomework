mystr = input()
newstr = ""
maxlenstr=''
for i in range(len(mystr)):
    if mystr[i] not in newstr:
        newstr = newstr + mystr[i]
        if len(newstr) > len(maxlenstr):
            maxlenstr = newstr
    else:
        if len(newstr) > len(maxlenstr):
            maxlenstr = newstr
        newstr = mystr[i]
print(maxlenstr)