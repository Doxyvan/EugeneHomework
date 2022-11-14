from itertools import combinations, count
from math import comb, factorial
def calc(colors, bags): #в википедии написано про числа стирлинга второго порядка, где n - colors; k - bags 
    coeff = 1/factorial(bags)
    summ = 0

    for i in range(bags+1):
        multipl1 = (-1)**(bags+i)
        multipl2 = comb(bags,i) * i**(colors)
        summ+= multipl1*multipl2

    print(summ*coeff)

def main():
    input_for_rebus = [int(x) for x in input().split()]
    if input_for_rebus[0]<input_for_rebus[1]:
        print("No solution")
    calc(input_for_rebus[0], input_for_rebus[1])
if __name__=="__main__":
    main()