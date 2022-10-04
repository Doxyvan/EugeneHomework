
def main1():
    mystr = input()
    firstLenOfMystr = len(mystr)
    num = int(input())
    newstr = ""
    k=num*2-2
    kchet = 0
    step = 0
    cntforchet = 1
    j = 0 
    for i in range(num):
        kchet = (i)*2 #Пропуск, который я буду использовать в четный шаг микро-цикла

        #Для num = 1 или если num больше длины нашего слова выводим изначальную строку
        if num == 1 or num >= firstLenOfMystr:
            print(mystr)
            break
        while (j)<len(mystr):
            if ((i!=num//2 and num>4) or num>3) and i!=0 and i!=num-1 and num <= firstLenOfMystr//2 + 1: #Работает для тех чисел, которые делят слово так, чтобы в первой строчке было минимум две буквы
                if cntforchet%2!=0 and j==step: #Нечетный шаг микро-цикла, используем проход через каждые K элементов, где k0 = num*2-2, k1=k0-2, kn=k(n-1)-2
                    newstr = newstr + mystr[j]
                    cntforchet +=1
                    step+=k
                    print("Нечетный", mystr[j])
                elif cntforchet%2==0 and j==step:
                    newstr = newstr + mystr[j]
                    cntforchet +=1
                    step+=kchet
                    print("Четный", mystr[j])
                 
            #Алгоритм, работающий для 1<num<=3 и для num > (длины начального слова + 1)
            else:
                if ((j)%k == 0 and len(newstr)<firstLenOfMystr and 1<num<=3) or ((j)%k == 0 and j<=k and len(newstr)<firstLenOfMystr and num >= firstLenOfMystr//2 + 1) :
                    newstr = newstr + mystr[j]
                    print("Иначе", mystr[j], k, j, len(mystr))
           
            j += 1
        step=0
        j=0
        k-=2
        mystr = mystr[1:]
        if k == 0:
            k=num*2-2
    print(newstr)


if __name__ == "__main__":
    main1()
