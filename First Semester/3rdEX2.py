import math
from pickle import TRUE
import os





def main():
    begining = input()
    answer = [[begining]] + []
    global workb
    workb= [x for x in begining] #Лист, в котором будем делать перестановки и сохранять их в ответе
    global workb_step_back
    workb_step_back = []
    global checkPosition
    checkPosition = False
    for i in range(len(workb)-2):
        k = [workb.copy()]
        workb_step_back = workb_step_back + k
    global factorials
    factorials = dict()
    if len(begining)==2:
        answer.append([begining[::-1]])
        print (answer)
        return (answer)

    elif len(begining)==1:
        print (answer)
        return (answer)
    
    else:

        for i in range(2,len(begining)):
            factorials[i] = math.factorial(i)

        cnt_for_step = 0 #определяет, сколько комбинаций прошли,
                        # чтобы при cnt_for_step = math.factorial(n) сделать соотвествующий ему сдвиг

        for cnt_for_step in range(2,math.factorial(len(begining))+1):
            if check(cnt_for_step, factorials) != False:
                i = check(cnt_for_step, factorials)
                k=workb[-( i[0]+1)]
                workb = i[1]
                workb.pop(-(i[0]+1))
                workb.append(k)
                checkPosition = True
                check(cnt_for_step, factorials)
                if ["".join(workb)] not in answer:
                    answer.append(["".join(workb)]+[])

            elif cnt_for_step%2==0:
                k =  workb[-1]
                workb[-1] = workb[-2]
                workb[-2] = k 
                if ["".join(workb)] not in answer:
                    answer.append(["".join(workb)]+[])
                workb = workb_step_back[0] + []

            elif cnt_for_step%2!=0:
                k = workb[-3]
                workb = check(cnt_for_step, factorials)[1]
                workb.pop(-3)
                workb.append(k)
                
                if ["".join(workb)] not in answer:
                    answer.append(["".join(workb)]+[])


        print(answer)
        return (answer)


def check(n, lst):
    j = 0
    for divider in lst:
        if (n-1) % lst[divider] ==0:
            j = int(divider)
    if j!=0:
        global checkPosition
        global workb
        if j==2:
            workb_step_back[j-2] = workb.copy()
            checkPosition = False
        elif checkPosition == True:
            for i in range(j-1):
                workb_step_back[i] = workb.copy()
            checkPosition = False
        return [j, workb_step_back[j-2].copy()]

    return False

        

if __name__=="__main__":
    main()

""" 123-132-231-213-312-321 (начало+переворот+сдвиг+переворот+сдвиг+переворот)
    123-132-321-312-213-231


    1234-1243-1342-1324-1423-1432 Каждые 6 раз делается общий сдвиг влево,
    2341-2314-2413-2431-2134-2143 однако в остальном алгоритм для элементов такой же,
    3412-3421-3124-3142-3214-3241 как и сверху.
    4123-4132-4231-4213-4312-4321 Для k элементов все будет точно так же, но главный сдвиг (смена первого числа), происходит каждые
                                  math.factorial(n), где n = k-1.

    ['1234'], ['1243'], ['1342'], ['1324'], ['1423'], ['1432'],
    ['2341'], ['2314'], ['2413'], ['2431'], ['2134'], ['2143'],
    ['3412'], ['3421'], ['3124'], ['3142'], ['3241'], ['3214'],
    ['4123'], ['4132'], ['4231'], ['4213'], ['4312'], ['4321']


    ['12345'], ['12354'], ['12453'], ['12435'], ['12534'], ['12543'],
    ['13452'], ['13425'], ['13524'], ['13542'], ['13245'], ['13254'],
    ['14523'], ['14532'], ['14235'], ['14253'], ['14352'], ['14325'],
    ['15234'], ['15243'], ['15342'], ['15324'], ['15423'], ['15432'],
    
    ['23451'], ['23415'], ['23514'], ['23541'], ['23145'], ['23154'],
    ['24513'], ['24531'], ['24135'], ['24153'], ['24351'], ['24315'],
    ['25134'], ['25143'], ['25341'], ['25314'], ['25413'], ['25431'],
    ['21345'], ['21354'], ['21453'], ['21435'], ['21534'], ['21543'],
    
    ['34512'], ['34521'], ['34125'], ['34152'], ['34251'], ['34215'],
    ['35124'], ['35142'], ['35241'], ['35214'], ['35412'], ['35421'],
    ['31245'], ['31254'], ['31452'], ['31425'], ['31524'], ['31542'],
    ['32451'], ['32415'], ['32514'], ['32541'], ['32145'], ['32154'],
    
    ['45123'], ['45132'], ['45231'], ['45213'], ['45312'], ['45321'],
    ['41235'], ['41253'], ['41352'], ['41325'], ['41523'], ['41532'],
    ['42351'], ['42315'], ['42513'], ['42531'], ['42135'], ['42153'],
    ['43512'], ['43521'], ['43125'], ['43152'], ['43251'], ['43215'],
    
    ['51234'], ['51243'], ['51342'], ['51324'], ['51423'], ['51432'],
    ['52341'], ['52314'], ['52413'], ['52431'], ['52134'], ['52143'],
    ['53412'], ['53421'], ['53124'], ['53142'], ['53241'], ['53214'],
    ['54123'], ['54132'], ['54231'], ['54213'], ['54312'], ['54321']

    Для двух элементов:
    12
    21 (Смена главного числа произошла после math.factorial(n-1) комбинаций, где n=2)
    Для трех элементов:
    123-132
    231-213
    312-321 (Смена происходила каждые math.factorial(n-1), где n=3)
    
    Т.о. необходимо реализовать внутренние сдвиги (1234-1342-1423) и внешние сдвиги (1234-2341) и
    смены крайних двух элементов каждый сдвиг
    
"""