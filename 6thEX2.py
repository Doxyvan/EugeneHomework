def calc(mystr):
    complicatedNum = {
        "IV": 5,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 500,
        "CM": 900
    }
    mysum = 0
    isHere = True
    while isHere == True:
        isHere = False
        if "IV" in mystr:
            mystr = mystr.replace("IV", "", 1)
            mysum += 4
            isHere = True
        elif "IX" in mystr:
            mystr = mystr.replace("IX", "", 1)
            mysum += 9
            isHere = True
        elif "XL" in mystr:
            mystr = mystr.replace("XL", "", 1)
            mysum += 40
            isHere = True
        elif "XC" in mystr:
            mystr = mystr.replace("XC", "", 1)
            mysum += 90
            isHere = True
        elif "CD" in mystr:
            mystr = mystr.replace("CD", "", 1)
            mysum += 400
            isHere = True
        elif "CM" in mystr:
            mystr = mystr.replace("CM", "", 1)
            mysum += 900
            isHere = True
        if isHere == False:
            break
    
    for i in range(len(mystr)):
        if "I" in mystr:
            mystr = mystr.replace("I", "", 1)
            mysum += 1
        elif "V" in mystr:
            mystr = mystr.replace("V", "", 1)
            mysum += 5
        elif "X" in mystr:
            mystr = mystr.replace("X", "", 1)
            mysum += 10
        elif "L" in mystr:
            mystr = mystr.replace("L", "", 1)
            mysum += 50
        elif "C" in mystr:
            mystr = mystr.replace("C", "", 1)
            mysum += 100
        elif "D" in mystr:
            mystr = mystr.replace("D", "", 1)
            mysum += 500
        elif "M" in mystr:
            mystr = mystr.replace("M", "", 1)
            mysum += 1000
    return mysum
def main():
    inputForRIM = input()
    print(calc(inputForRIM))

if __name__ =="__main__":
    main()