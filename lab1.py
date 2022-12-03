

def recursion(mylist, current_num, current_sum, bag_of_signs, goal, sign):
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
    input_list = [int(x) for x in input().split()]
    goal = input_list[-1]
    working_list = input_list[1:len(input_list)-1]

    answering_list = recursion(working_list, 0, 0, [], goal, 1)
    answering_list = answering_list[::-1 ]
    answer = []
    point = 0
    for i in range(1, len(working_list)+1):
        if working_list[-i] * answering_list[point] < 0:
            answer.append(str(answering_list[point]*working_list[-i]))
            point += 2**(i)

        else:
            answer.append("+"+str(answering_list[point]*working_list[-i]))
            point+=1
    answer[len(answer)-1] = answer[len(answer)-1][1:]
    answer = answer[::-1]
    print("".join(answer))
    


if __name__ == "__main__":
    main()