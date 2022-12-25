import copy
import sys

def matrix(n):
    wmatrix = []
    row = ["0"] * n
    for _ in range(n):
        wmatrix.append(copy.deepcopy(row))
        
    return wmatrix

def output(list_with_numbers, one_more_piece, n):
    list_with_numbers.append(one_more_piece)
    for piece in range(len(list_with_numbers)):
        t_row=(list_with_numbers[piece])//n
        t_col=(list_with_numbers[piece])%n
        coordinates = (t_col, t_row)
        f.write(str(coordinates))
    f.write("\n")

def find_free_square(wmatrix, n, previous_free_square):
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if wmatrix[row][col] == "0":
                return (row*n)+col

def set_up_new_pieces(free_square, wmatrix, n, current_piece, l, new_pieces, wmatrix_clones, step):
    
    if free_square is not None and current_piece<l:
        wmatrix = set_up_piece(wmatrix, free_square, n, str(current_piece))
        if current_piece+1<l:
            wmatrix_clones[current_piece] = copy.deepcopy(wmatrix)
        new_pieces[current_piece-1]=free_square
        
        free_square = find_free_square(wmatrix, n, free_square)
        set_up_new_pieces(free_square, wmatrix, n, current_piece+1, l, new_pieces, wmatrix_clones,step+1)

    else:
        if step<0:
            f.close()
            return 0
        if free_square is not None:
            p_row = (free_square//n)
            p_col = (free_square%n)
            p_col_copy = p_col
            for row in range(p_row, n):
                    if row > p_row:
                        p_col_copy = 0
                    for col in range(p_col_copy, n):
                        if wmatrix[row][col] == "0":
                            print(new_pieces[:-1], row*n+col)
                            #output(new_pieces[:-1], row*n+col, n)
        wmatrix = copy.deepcopy(wmatrix_clones[step])
        wmatrix[(new_pieces[step])//n][(new_pieces[step])%n] = "H"
        for mc in range(step, l-1):
                wmatrix_clones[mc] = copy.deepcopy(wmatrix)
        free_square = find_free_square(wmatrix, n, (new_pieces[step]))
        set_up_new_pieces(free_square, wmatrix, n, step+1, l, new_pieces, wmatrix_clones, step-1)

def set_up_piece(wmatrix, pos, n,  piece = "#"):
    row = (pos//n)
    col = (pos%n)
    wmatrix[row][col] = piece
    for i in range(5):
        if i%2==0:
            for m in range(-1,2,2):
                if n>row+(i-2) >= 0 and n>col+m>=0:
                    wmatrix[row+(i-2)][col+m] = "*"
        else:
            for m in range(-2,3):
                if n>row+(i-2) >= 0 and n>col+m>=0:
                    wmatrix[row+(i-2)][col+m] = "*"
    return wmatrix

def main():
    global f
    f = open("Output_Lab_2.txt", "w")
    sys.setrecursionlimit(1000000000)
    step = -1
    n, l, k = list(map(int, input().split()))
    new_pieces = [-1]*l
    wmatrix = matrix(n)
    for _ in range(k):
        x, y = list(map(int, input().split()))
        pos = y*n + x
        wmatrix = set_up_piece(wmatrix, pos, n)
    wmatrix_clones = [copy.deepcopy(wmatrix)]*(l-1)
    free_square = find_free_square(wmatrix, pos, 0)

    set_up_new_pieces(free_square, wmatrix, n, 1, l, new_pieces, wmatrix_clones, step)

if __name__ == "__main__":
    main()