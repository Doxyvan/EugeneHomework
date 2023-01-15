

def recursion(mylist: list, current_num: int, current_sum: int, bag_of_signs: list, goal: int, sign: int) -> list:
    current_sum += (mylist[current_num]) * sign 
    bag_of_signs.append(sign)

    current_num+=1

    if current_num+1 <= len(mylist):
        return recursion(mylist, current_num, current_sum, bag_of_signs, goal, 1) or recursion(mylist, current_num, current_sum, bag_of_signs, goal, -1)
    
    else:
        if current_sum == goal:
            return bag_of_signs
        else:
            return
   

def main():
    input_list = open("inputLab1.txt", "r").readline() #Считываем
    #input_list = [int(x) for x in input().split()]  
    #
    goal = input_list[-1] #Крайнее число - цель
    working_list = input_list[1:len(input_list)-1] #Отсекаем числа, с которыми собираемся работать

    answering_list = recursion(working_list, 0, 0, [], goal, 1) #Входим в рекурсию
    if answering_list is None:
        print("No solution")
        return
    answering_list = answering_list[::-1 ] #Разворачиваем лист со знаками для удобства сортировки
    answer = [] #Пустой лист, куда будет записываться итог работы алгоритма
    point = 0
    for i in range(1, len(working_list)+1):
        if working_list[-i] * answering_list[point] < 0: #Если число отрицательное
            answer.append(str(answering_list[point]*working_list[-i])) #Добавляем строковое в массив ответа число с его знаком
            point += 2**(i) #Следующий знак будет иметь индекс на 2**(уровень старшинства) больше

        else:
            answer.append("+"+str(answering_list[point]*working_list[-i]))
            point+=1
    answer[len(answer)-1] = answer[len(answer)-1][1:] #Разворачиваем
    answer = answer[::-1]
    print("".join(answer))
    


if __name__ == "__main__":
    main()