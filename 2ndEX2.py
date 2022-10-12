
def main1():
    mystr = input()
    mystr = mystr.split()
    mystr = (mystr[::-1])
    newstr = ""
    for i in range(len(mystr)):
        newstr = newstr + " " + mystr[i]
    print((newstr.strip()).capitalize())

        
if __name__ == "__main__":
    main1()
