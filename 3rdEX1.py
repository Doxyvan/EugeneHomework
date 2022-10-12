


def main():
    worklist = list(map(int, input().split())) #Список, куда вводятся данные
    l = [] # Лист с кратким именем, с которым быстро можно работать
    lanswer = []
    if len(worklist)<4:
        print(False)
    
    else:
        c = int(input()) # Цель итоговая
        worklist.sort()
        if c <= sum(worklist[:4]):
            print(worklist[:4])
        elif c >= sum(worklist[len(worklist)-4:]):
            print(worklist[len(worklist)-4:])
        else:
            #Выбираю одно число из списка, максимально близкое к цели, удаляю его и вставляю в итоговый (Пункт 1)
            #Затем прохожусь по списку так, чтобы выбрать пару чисел, которые в сумме максимально близки к нулю, но к тому же приближают к цели (Пункт 2)
            #Удаляю эту пару из списка и прохожусь еще раз, чтобы найти число, приближающее меня к цели (Пункт 3)
            minRadius = 99999
            firstnum, firstIndex = 0, 0
            second = [] #Складирую пары чисел, максимально приближающих меня к 0
            sumka = []
            for i in range(len(worklist)):
                if abs(worklist[i] - c) < minRadius and ((worklist[i]<0 and c<0) or (worklist[i]>0 and c>0)):
                    firstnum = worklist[i]
                    minRadius = abs(worklist[i]-c)
                    firstIndex = i
            worklist.pop(firstIndex)

            for j in range(len(worklist)-1):
                for n in range(j+1, len(worklist)):
                    second.append([worklist[j], worklist[n]])

            minRadius=99999
            for i in range(len(second)):
                if firstnum == c:
                    k = [x for x in worklist if x not in second[i]]
                else:
                    k = [x for x in worklist if x not in second[i]] + [firstnum]
                for n in range(len(k)):
                    if abs(c-abs(sum(second[i])+k[n])) < minRadius:
                        minRadius = abs(c-abs(sum(second[i])+k[n]))
                        sumka.append(second[i]+[k[n]])
            #Перепроверка ответа
            minRadius = 99999
            minfirst = 0
            if firstnum == c:
                    k = [x for x in worklist if x not in sumka[-1]]
            else:
                k = [x for x in worklist if x not in sumka[-1]] + [firstnum]
            for i in range(len(k)):
                if abs(c - (k[i] + sum(sumka[len(sumka)-1]))) < minRadius:
                    minfirst = k[i]
                    minRadius =abs(c- (k[i] + sum(sumka[len(sumka)-1])))
            
            if abs(c - sum([minfirst]+sumka[len(sumka)-1])) <= abs(c - sum([firstnum]+sumka[len(sumka)-1])):
                print([minfirst]+sumka[len(sumka)-1])
            else: 
                print([firstnum]+sumka[len(sumka)-1])

if __name__ == "__main__":
    main()