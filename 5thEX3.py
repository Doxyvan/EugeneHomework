from operator import index


neighbours = {
        "1": [1, 2, 4],
        "2": [2, 1, 3, 5],
        "3": [3, 2, 6],
        "4": [4, 1, 5, 7],
        "5": [5,2,4,6,8],
        "6": [6,3,5,9],
        "7": [7,4,8],
        "8": [8,5,7,9,0],
        "9": [9,6,8],
        "0": [0,8]
    }
cnt_of_neighbours = []#этап для каждого числа
answer = []
deviders =[]
cnt_of_variants = 1
step = 0
neighbour_step = 0
def stages(num, mystr, clone, dev, con = cnt_of_neighbours):
    step = 0
    for n in range(len(dev)):
        if (num+1)%dev[n]==0:
           step = n
    if step == 0:
        cnt_of_neighbours[step] += 1
        mystr[-(step+1)] = str(neighbours[main_mystr[-(step+1)]][cnt_of_neighbours[step]])
        clone[-(step+1)] = mystr.copy()
    elif step != 0:
            mystr = clone[-(step+1)].copy()
            cnt_of_neighbours[step] += 1
            mystr[-(step+1)] = str(neighbours[main_mystr[-(step+1)]][cnt_of_neighbours[step]])
            for i in range(-(step+1), 0):
                clone[i] = mystr.copy()
            for i in range(step):
                cnt_of_neighbours[i] = 0

    answer.append("".join(clone[-1]))
    return mystr,clone

    


def get_pins(mystr):
    mystr = [x for x in mystr]
    global main_mystr
    main_mystr = mystr.copy()
    cnt_of_variants = 1
    deviders = [] #иснструкции по обороту чисел
    clone_mystr=[mystr.copy()]*len(mystr)
    for i in range(len(mystr)-1, -1, -1): #Составляю кол-во всех вариантов + наполняю лист, где хранятся инструкции по обороту чисел
        deviders.append(cnt_of_variants)
        cnt_of_variants*= len(neighbours[mystr[i]])

    for i in range(cnt_of_variants-1):
        k = stages(i, mystr, clone_mystr, deviders)
        mystr = k[0]
        clone_mystr = k[1]

    print(answer)
    return 

def main():
    mystr = input()
    answer.append(mystr)
    global cnt_of_neighbours
    cnt_of_neighbours = [0]*len(mystr) 
    get_pins(mystr)
    
if __name__ == "__main__":
    main()


# 123 - 122 - 126 - 113 - 112- 116 - 133 - 132 - 136 - 153 - 152 - 156
# то же самое, что и предыдущая, но на первом месте 2
# то же самое, что и предыдущая, но на первом месте 4

""" Output with input = 123
  '123', '122', '126', '113', '112', '116', '133', '132', '136', '153', '152', '156',
  '223', '222', '226', '213', '212', '216', '233', '232', '236', '253', '252', '256',
  '423', '422', '426', '413', '412', '416', '433', '432', '436', '453', '452', '456'

"""

# 123-122-126 [кол-во соседей n разряда] -> смена n+1 рязряда
#произошло [кол-во соседей n+1 разряда] -> сменя n+2 разряда