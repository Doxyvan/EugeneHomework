from collections import namedtuple
bank = namedtuple("Bank", ("name", "cash"))

def main():
    summ = 0
    n = int(input())
    mybanks = []
    for _ in range(n):
        k = [x for x in input().split()]
        mybanks.append(bank(k[0], k[1]))
    i, j = 0, 2
    myMaxList=[0]*n #Листик, где будут сохраняться максимальные значения на данный момент
    myMaxList[0] = int(mybanks[0].cash)
    myMaxList[1] = max(int(mybanks[0].cash), int(mybanks[1].cash))

    for i in range(2, n):
        myMaxList[i] = max(myMaxList[i - 2] + int(mybanks[i].cash), myMaxList[i - 1])


    print(myMaxList[i]) #Вывод последнего элемента, ибо в нем хранится максимальный элемент

if __name__ == "__main__":
    main()

