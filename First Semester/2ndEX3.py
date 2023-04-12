from inspect import isclass
from  operator import truediv
from symbol import expr_stmt
def main1():
    mystr = input()
    mystrClone = mystr
    isClear = False
    maxstr = ""

    k1 = mystr.find("()")
    k2 = mystr.find("{}")
    k3 = mystr.find("[]")

    if k1==-1 and k2==-1 and k3==-1:
        print(False)
    depth = 0 #Глубина вложенности скобок
    i = 0 #Кол-во подряд идущих открывающихся, если i>1, то глубина начисляется за каждую открывающуюся
    open=[123,91,40]
    close=[125,93,41]

    


    str_with_classes_of_depth = []
    while isClear != True:
        newstr = "" #Строчка для динамического прохода
        lenOfNewstr = 0 #Длина для работы с закрывающимися скобками
        maxstr = "" #Ответ итоговый
        kWhenBreak = 0 #Этот коэффициент нужен, чтобы удерживать n в разумных значениях после обнуления строки
        balancecoeff = 0 #Коэффициент для баланса, если он равен 0 и следующая скобка закрытая, то можно сворачиваться. Если же он равен 0 и следующая скобка открытая,
                        #то продолжаем пересчитывать скобки вплоть до предыдущего условия.
        i = 0
        firstExistence = 0 #Коэффициент наличия первой скобочки, которая закрывается в самом конце; пример {([()])()[]}, где фигурные скобки - предмет взаимодействия коэффициента
        for n in range(len(mystrClone)):
            if ord(mystrClone[n]) in open:
                i+=1
                str_with_classes_of_depth.append(mystrClone[n]+"-"+str(depth))
                newstr = newstr + mystrClone[n]
                if n == 0:
                    firstExistence = 1 #Открытие главной скобки
                balancecoeff+=1
                if n+1<=len(mystrClone)-1:
                    if ord(mystrClone[n+1]) in close:
                        i=0
                        lenOfNewstr = len(newstr)
                    elif ord(mystrClone[n+1]) in open:
                        i+=1
                        if i>1: #Для наглядности идеи глубины скобок
                            depth+=1
                
            elif ord(mystrClone[n]) in close:
                #Вход для первого итерации цикла
                if i == 0:
                    i+=1

                str_with_classes_of_depth.append(mystrClone[n]+"-"+str(depth)) #Для наглядности идеи глубины скобок
                

                
                if len(newstr) == 0:
                    kWhenBreak = n+1
                    if n+1<=len(mystrClone)-1:
                        if ord(mystrClone[n+1]) in open:
                            i=0
                        elif ord(mystrClone[n+1]) in close:
                            i+=1
                            if i>1:
                                depth-=1
                    continue


            
                
                elif -len(newstr) <= lenOfNewstr-(n-kWhenBreak)-i < len(newstr):
                    if (ord(newstr[lenOfNewstr-(n-kWhenBreak)-i])+1 == ord(mystrClone[n])) or (ord(newstr[lenOfNewstr-(n-kWhenBreak)-i])+2 == ord(mystrClone[n])) and balancecoeff > 0:
                        newstr = newstr + mystrClone[n]
                        lenOfNewstr = len(newstr)
                        balancecoeff -= 1
                        if balancecoeff == 0:
                            firstExistence = 0 #Закрытие первой скобки произошло в середине, т.е. нет обложки для внутренних скобок
                        if len(newstr) > len(maxstr):
                            maxstr = newstr
                        #print(newstr)
                    elif n == len(mystrClone)-1 and firstExistence == 1 and (ord(newstr[0])+1!=ord(mystrClone[n]) and ord(newstr[0])+2!=ord(mystrClone[n])) :
                        newstr = newstr[1:]
                    elif n == len(mystrClone)-1 and firstExistence == 1 and (ord(newstr[0])+1==ord(mystrClone[n]) or ord(newstr[0])+2==ord(mystrClone[n])) and balancecoeff == 1: #Этот elif и последующий выполняют одну и ту же функцию, но этот сделан для закрытия ГЛАВНЫХ скобок, а следующий для внутренних
                        newstr = newstr + mystrClone[n]
                        lenOfNewstr = len(newstr)
                        firstExistence=0
                        balancecoeff -=1
                        if len(newstr) > len(maxstr):
                            maxstr = newstr
                    
                    else:
                        newstr = ""
                        if n==len(mystrClone)-1 and firstExistence == 1:
                            print(maxstr[1:])
                            return
                        firstExistence = 0 #Произошла поломка всей подстроки, так что первый удаляется тоже
                        balancecoeff = 0
                        kWhenBreak = n

                #Прогнозирование следующих скобок
                if n+1<=len(mystrClone)-1:
                    if ord(mystrClone[n+1]) in open:
                        i=0
                    elif ord(mystrClone[n+1]) in close:
                        i+=1
                        if i>1:  #Для наглядности идеи глубины скобок
                            depth-=1
                            
        if firstExistence==1:
            maxstr = maxstr[1:]
            mystrClone = maxstr
            if len(maxstr) == len(mystrClone):
                isClear = True
        else:
            if len(maxstr) == len(mystrClone):
                isClear = True
            else:
                mystrClone = maxstr
            
    if len(maxstr) == len(mystr):
        print(True)
    else:
        print(maxstr)

        
    #print(str_with_classes_of_depth)

if __name__ == "__main__":
    main1()
