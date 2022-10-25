from itertools import combinations
def main():
    mylist = [x for x in input().split()]
    answer = []
    for i in range(len(mylist)+1):
        comboVombo = list(combinations(mylist,i))
        for n in comboVombo:
            answer.append(n)
    print(set(answer))

if __name__=="__main__":
    main()