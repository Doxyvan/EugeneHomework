import numpy as np

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
    mymytrix = ["0"]*num*num
    mymytrix = np.reshape(mymytrix, (num,num))
    return mymytrix

def main():
    global n
    n, l, k = list(map(int, input().split())) #Размерность матрицы n*n, l - кол-во фигур, которое надо расставить, k - кол-во фигур, которые уже стоят
    global new_pieces
    new_pieces = l*[0]
    global matrix_copies
    matrix_copies = []
    curcle = 0
    mymatrix = matrix(n)
    for pieces in range(k):
        x, y = list(map(int, input().split()))
        number_of_square = (y-1)*n+x
        mymatrix = set_up_piece(mymatrix, number_of_square-1)
        
    for _ in range(l):
        matrix_copies.append(mymatrix.copy())

    free_square = find_free_square(mymatrix, 0)
    set_up_new_pieces(free_square, 0, l, mymatrix, curcle)

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
                            matrix_copies[current_piece+1] = matrix.copy()
                            break
                else:
                    break
            new_pieces[current_piece] = (row-1)*n+col +1
            new_free_square = find_free_square(matrix, free_square)
            return set_up_new_pieces(new_free_square, current_piece+1, cnt_of_pieces, matrix, curcle)
        else:
            for row in range(p_row, n):
                if row > p_row:
                    p_col_copy = 0

                for col in range(p_col_copy, n):
                    if matrix[row][col] == "0":
                        print(new_pieces, (row)*n+col+1)
                curcle = 1

            matrix_copies[current_piece] = matrix_copies[current_piece-curcle].copy()
            matrix = matrix_copies[current_piece].copy()
            matrix[(new_pieces[current_piece-curcle]-1)//n][(new_pieces[current_piece-curcle]-1)%n] = "H"

            for mc in range(current_piece-curcle, cnt_of_pieces):
                matrix_copies[mc] = matrix.copy()
            new_free_square = find_free_square(matrix, new_pieces[current_piece-curcle])
            return  set_up_new_pieces(new_free_square, current_piece-curcle, cnt_of_pieces, matrix, curcle)
    else:
        curcle += 1
        if current_piece-curcle<0:
            return
        else:
            matrix_copies[current_piece] = matrix_copies[current_piece-curcle].copy()
            matrix = matrix_copies[current_piece].copy()
            matrix[(new_pieces[current_piece-curcle]-1)//n][(new_pieces[current_piece-curcle]-1)%n] = "H"
            for mc in range(current_piece-curcle, cnt_of_pieces):
                matrix_copies[mc] = matrix.copy()
            new_free_square = find_free_square(matrix, new_pieces[current_piece-curcle])
            return  set_up_new_pieces(new_free_square, current_piece-curcle, cnt_of_pieces, matrix, curcle)
if __name__ == "__main__":
    main()