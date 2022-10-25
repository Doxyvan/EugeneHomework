def main1():
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

            length = len(newstr)
            if mystr[i] == newstr[-length]:
                newstr = newstr[-length+1:]
                newstr = newstr + mystr[i]
            else:
                newstr = mystr[i]
    print(maxlenstr)

if __name__ == "__main__":
    main1()
