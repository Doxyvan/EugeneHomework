import copy
import time

def output(list_with_numbers: list, n: int, condition_pieces:tuple) -> None:
    for piece in condition_pieces:
        f.write(str(piece))
    for piece in range(len(list_with_numbers)):
        t_row=(list_with_numbers[piece])//n
        t_col=(list_with_numbers[piece])%n
        coordinates = (t_col, t_row)
        f.write(str(coordinates))
    f.write("\n")

def step_back(wmatrix: list, wmatrix_clones: list, n: int, end: int, new_pieces: list) -> tuple:
    l = len(new_pieces)
    step = 0
    for i in range(l-1):
        if new_pieces[i] != end and new_pieces[i+1]==end:
            step = (i-l)
    if step == 0: 
        return
    wmatrix = copy.deepcopy(wmatrix_clones[step+1])
    row = new_pieces[step]//n
    col = new_pieces[step]%n
    wmatrix[row][col] = "H"
    for mc in range(step+1, 0):
        wmatrix_clones[mc] = copy.deepcopy(wmatrix)
    step = step + l

    for i in range(step, l-1):
        free_square = find_free_square(wmatrix, n, new_pieces[step])
        if free_square is not None:
            wmatrix_clones[i] = copy.deepcopy(wmatrix)
            wmatrix = set_up_piece(wmatrix, free_square, n)
            new_pieces[i] = free_square
        else:
            break
    return wmatrix, wmatrix_clones, new_pieces

def working(wmatrix: list, n: int, new_pieces: list, condition_pieces:tuple) -> tuple:
    global outputTheBoard
    global cnt
    wmatrix_clones = [0]*(len(new_pieces)-1)
    end = find_last_free_square(wmatrix, n, 0)
    for i in range(len(new_pieces)-1):
        free_square = find_free_square(wmatrix, n, 0)
        wmatrix_clones[i] = copy.deepcopy(wmatrix)
        wmatrix = set_up_piece(wmatrix, free_square, n)
        new_pieces[i] = free_square
    
    
    while new_pieces[0] != n*n -1:
        free_square = find_free_square(wmatrix, n, new_pieces[-2])
        if free_square is not None:
            p_row = (free_square//n)
            p_col = (free_square%n)
            for row in range(p_row, n):
                if row > p_row:
                        p_col = 0
                for col in range(p_col, n):
                    if wmatrix[row][col] == "0":
                        new_pieces[-1] = row*n+col
                        cnt+=1
                        output(new_pieces, n, condition_pieces)
                        if outputTheBoard == False:
                            matrix_for_output = copy.deepcopy(wmatrix)
                            matrix_for_output = set_up_piece(matrix_for_output, find_free_square(matrix_for_output, n), n)
                            for i in range(n):
                                print(matrix_for_output[i])
                            outputTheBoard = True

        end = find_last_free_square(wmatrix, n, 0)
        ret_step_back = step_back(wmatrix, wmatrix_clones, n, end, new_pieces)
        if ret_step_back is None:
            return
        else:
            wmatrix, wmatrix_clones, new_pieces = ret_step_back
    
    
def main():
    global cnt
    cnt = 0
    now = time.time()
    global f
    with open("Input_Lab_2.txt", "r") as in_data_elder:
        in_data = [x.replace("\n", "") for x in in_data_elder]
    f = open("Output_Lab_2.txt", "w")
    global outputTheBoard
    outputTheBoard = False
    n, l, k = list(map(int, in_data[0].split()))
    in_data = in_data[1:]
    new_pieces = [-1]*l
    wmatrix = matrix(n)
    condition_pieces = []
    for index in range(k):
        coordinates = in_data[index].split()
        x, y = coordinates
        x, y = int(x), int(y)
        condition_pieces.append((x,y))
        pos = y*n + x
        wmatrix = set_up_piece(wmatrix, pos, n)
    
    working(wmatrix, n, new_pieces, condition_pieces)
    f.close()
    print(cnt)
    end = time.time()
    #print(end-now)

def matrix(n):
    wmatrix = []
    row = ["0"] * n
    for _ in range(n):
        wmatrix.append(copy.deepcopy(row))
        
    return wmatrix


def set_up_piece(wmatrix: list, pos: int, n: int,  piece = "#") -> list:
    if pos is not None:
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

def find_free_square(wmatrix: list, n:int, previous_free_square=0) -> int:
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if wmatrix[row][col] == "0":
                return (row*n)+col

def find_last_free_square(wmatrix:list, n:int, previous_free_square=0) -> int:
    k = -1
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if wmatrix[row][col] == "0":
                k = (row*n)+col
    if k == -1:
        return find_last_piece_square(wmatrix, n, 0)
    return k

def find_last_piece_square(wmatrix: list, n: int, previous_free_square=0) -> int:
    j = 0
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if wmatrix[row][col] == "#":
                j = (row*n)+col
    return j

if __name__ == "__main__":
    main()