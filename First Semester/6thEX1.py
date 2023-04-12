

def santa_users(mylist):
    d = dict()
    for i in range(len(mylist)):
        if len(mylist[i]) == 2:
            mylist[i][1] = str(mylist[i][1]).replace(" ", "")
            if mylist[i][1] in "":
                d[mylist[i][0]] = None
            else:
                d[mylist[i][0]] = mylist[i][1]
        else:
            d[mylist[i][0]] = None
    return d

def main():
    inputForSanta = [[x for x in input().split(",")] for j in range(int(input("Число пользователей:")))]
    #Сначала вводится число пользователей, затем строчки типа name surname, index
    print(santa_users(inputForSanta))
if __name__ =="__main__":
    main()