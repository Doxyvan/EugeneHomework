def main():
    mymatrix = [[11,12,13,14,15],
                [21,22,23,24,25],
                [31,32,33,34,35],
                [41,42,43,44,45],
                [51,52,53,54,55]]
    answer = []
    i, j = 0, 0 #i - какой элемент строки рассматриваем; j - номер строки

    while len(answer)<len(mymatrix)*len(mymatrix[0]):
        while 0<=i<len(mymatrix[j])-1:
            answer.append(mymatrix[j][i])
            mymatrix[j][i] = -1
            if mymatrix[j][i+1] != -1:
                i += 1
            else:
                j += 1
                break
        
        while 0<=j<len(mymatrix)-1:
            answer.append(mymatrix[j][i])
            mymatrix[j][i] = -1
            if mymatrix[j+1][i] != -1:
                j += 1
            else:
                i -= 1
                break
            
        while 0<=i<len(mymatrix[j]): 
            answer.append(mymatrix[j][i])
            mymatrix[j][i] = -1
            if mymatrix[j][i-1] != -1:
                i -= 1
            else:
                j -= 1
                break

        while 0<=j<len(mymatrix[j]):
            answer.append(mymatrix[j][i])
            mymatrix[j][i] = -1
            if mymatrix[j-1][i] != -1:
                j -= 1
            else:
                i += 1
                break

    print(answer[:len(mymatrix)*len(mymatrix[0])])
if __name__ == "__main__":
    main()