def main():
    mymatrix = [[11,12,13],
                [21,22,23],
                [31,32,33]]
    for i in range(len(mymatrix)):
        for n in range(i, len(mymatrix)):
            k = mymatrix[i][n]
            mymatrix[i][n] = mymatrix[n][i]
            mymatrix[n][i] = k
    for i in range(len(mymatrix)):
        mymatrix[i].reverse()
    print(mymatrix)

if __name__ == "__main__":
    main()