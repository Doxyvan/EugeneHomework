import numpy as np
import sys
def output(list_with_numbers, one_more_piece):
    list_with_numbers.append(one_more_piece)
    for piece in range(len(list_with_numbers)):
        t_row=(list_with_numbers[piece]-1)//n
        t_col=(list_with_numbers[piece]-1)%n
        coordinates = (t_col, t_row)
        f.write(str(coordinates))
    f.write("\n")
    return
    
    
        

def find_free_square(matrix, previous_free_square):
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if matrix[row][col] == "0":
                return (row*n)+col
def set_up_piece(matrix, k, piece = "F"):

    row = (k//n)
    col = (k%n)
    matrix[row][col] = piece
    for i in range(5):
        if i%2==0:
            for m in range(-1,2,2):
                if n>row+(i-2) >= 0 and n>col+m>=0:
                    matrix[row+(i-2)][col+m] = "X"
        else:
            for m in range(-2,3):
                if n>row+(i-2) >= 0 and n>col+m>=0:
                    matrix[row+(i-2)][col+m] = "X"
    return matrix

def matrix(num):
    mymytrix = []
    for _ in range(num):
        mymytrix.append(["0"]*num)
    return mymytrix

def main():
    global f
    f = open("Output_Lab_2.txt", "a")
    sys.setrecursionlimit(10000000)
    global n
    n, l, k = list(map(int, input().split())) #Размерность матрицы n*n, l - кол-во фигур, которое надо расставить, k - кол-во фигур, которые уже стоят
    global new_pieces
    new_pieces = l*[0]
    global matrix_copies
    matrix_copies = [0]*l
    curcle = 0
    mymatrix = matrix(n)
    for _ in range(k):
        x, y = list(map(int, input().split()))
        number_of_square = (y)*n+x
        mymatrix = set_up_piece(mymatrix, number_of_square)
      
    for ncopy in range(l):
        matrix_copies[ncopy] = [x[:] for x in mymatrix]
    free_square = find_free_square(mymatrix, 0)
    set_up_new_pieces(free_square, 0, l, mymatrix, curcle)
    f.close()
    

def set_up_new_pieces(free_square, current_piece, cnt_of_pieces, matrix, curcle = 0):
    breaker = False
    if not(free_square is None):
        p_row = free_square//n
        p_col = free_square%n
        p_col_copy = p_col
        if current_piece < cnt_of_pieces-1:
            for row in range(p_row, n+1):
                if breaker == False:
                    if row > p_row:
                        p_col_copy = 0
                    for col in range(p_col_copy , n):
                        if matrix[row][col] == "0":
                            name_of_current_piece = str(current_piece+1)
                            matrix = set_up_piece(matrix, (row)*n+col, name_of_current_piece)
                            breaker = True
                            matrix_copies[current_piece+1] = [x[:] for x in matrix]
                            break
                else:
                    break
            new_pieces[current_piece] = (row-1)*n+col +1
            new_free_square = find_free_square(matrix, free_square)
            set_up_new_pieces(new_free_square, current_piece+1, cnt_of_pieces, matrix, curcle)
        else:
            for row in range(p_row, n):
                if row > p_row:
                    p_col_copy = 0

                for col in range(p_col_copy, n):
                    if matrix[row][col] == "0":
                        output(new_pieces[:-1], (row)*n+col+1)
                curcle = 1

            matrix_copies[current_piece] = [x[:] for x in matrix_copies[current_piece-curcle]]
            matrix = [x[:] for x in matrix_copies[current_piece]]
            matrix[(new_pieces[current_piece-curcle]-1)//n][(new_pieces[current_piece-curcle]-1)%n] = "H"

            for mc in range(current_piece-curcle, cnt_of_pieces):
                matrix_copies[mc] = [x[:] for x in matrix]
            new_free_square = find_free_square(matrix, new_pieces[current_piece-curcle])
            set_up_new_pieces(new_free_square, current_piece-curcle, cnt_of_pieces, matrix, curcle)
    else:
        curcle += 1
        if current_piece-curcle<0:
            return
        else:
            matrix_copies[current_piece] = [x[:] for x in matrix_copies[current_piece-curcle]]
            matrix = [x[:] for x in matrix_copies[current_piece]]
            matrix[(new_pieces[current_piece-curcle]-1)//n][(new_pieces[current_piece-curcle]-1)%n] = "H"
            for mc in range(current_piece-curcle, cnt_of_pieces):
                matrix_copies[mc] = [x[:] for x in matrix]
            new_free_square = find_free_square(matrix, new_pieces[current_piece-curcle])
            set_up_new_pieces(new_free_square, current_piece-curcle, cnt_of_pieces, matrix, curcle)
if __name__ == "__main__":
    main()