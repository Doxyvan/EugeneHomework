import time
import pygame as pg
import exceptions
from gui import Game_Box, Box
from figure import King_Horse as kh_figure
from figure import Figure

class Game():
    
    def __init__(self, figure, f) -> None:
        self.figure = figure
        self.f = f
        self.cnt = 0
    
    def start(self):
        in_data = Box() #Создаем окно для ввода начальных значений
        in_data.wait_window() #Ждем отработки окна
        n, l, k = in_data.get_info() #Получаем информацию о поле и фигурах
        x, y = in_data.get_coords()  #Получаем координаты K-тых фигур
        in_data.mainloop() #Запускаем окно работать до закрытия

        #Если поле размерность 0x0, то и фигуру туда не поставить, а значит вывести "no solution"
        if n == 0: 
            self.output_message("no solution")
            self.f.close()
            return
        
        self.create_matrixes(n)
        self.start_time = time.time()

        
        board = Board(self.wmatrix, n, [-1]*l, [], l, k, self.matrix_for_pg, self.figure, self.f, self)
        for index in range(k):
            board.condition_pieces.append((x[index],y[index])) #Запись координат фигур
            pos = y[index]*n + x[index] #Перевод координат в порядковый номер
            board.set_up_piece(board.wmatrix, pos, n) #Постановка в консольной матрице
            #Постановка в матрице pygame
            self.matrix_for_pg.set_up_piece_for_tkinter(pos, n, (0,255,0), (0, 0, 255), self.figure)

        
        board.working()

        self.end()

    def create_matrixes(self, n):
        self.wmatrix = []
        row = ["0"] * n #Создаем строчку
        for _ in range(n):
            self.wmatrix.append([x for x in row]) #Множим эту строчку по числу n
        
        self.matrix_for_pg = Game_Box(n)

    #Функция для записи в файл определенного осообщения
    def output_message(self, msg:str) -> None:
        #msg - сообщение, которое передаем в файл
        self.f.write(msg)
        self.f.write("\n")
    def end(self):
        self.f.close()#Закрываем файл
        self.end = time.time()#Получаем время окончания работы
        print(self.end-self.start_time)#Выводим время работы
        print(self.cnt)#Выводим кол-во ходов
class Board():
    def __init__(self, wmatrix, n, new_pieces, condition_pieces, l, k, matrix_for_pg, figure, f, master) -> None:
        self.wmatrix = wmatrix
        self.n = n
        self.new_pieces = new_pieces
        self.condition_pieces = condition_pieces
        self.l = l
        self.k = k
        self.matrix_for_pg = matrix_for_pg
        self.figure = figure
        self.f = f
        self.master = master
        self.outputTheBoard = False
    
    def output(self) -> None:
        """
        Параметры:
        list_with_numbers - список порядковых номеров клеток на доске, на которых стоят фигуры
        n - размерность доски
        condition_pieces - кортеж координат фигур, которые были поставлены из условия
        """
        for piece in self.condition_pieces: #Для фигур из условия
            self.master.f.write(str(piece[::-1])) #Запись происходит по виду (y, x) или (row, col)
        for piece in range(len(self.new_pieces)): #Для фигур, расставляемых программно
            t_row=(self.new_pieces[piece])//self.n
            t_col=(self.new_pieces[piece])%self.n
            coordinates = (t_row,t_col)
            self.master.f.write(str(coordinates))
        self.master.f.write("\n")

    #Отступ для смены позиции очередной не "свободной" фигуры
    def step_back(self, wmatrix: list, wmatrix_clones: list, n: int, end: int, new_pieces: list) -> tuple:
        """
        Параметры:
        wmatrix - матрица для консольного вывода
        wmatrix_clones - список клонов матрицы для консольного вывода
        n - размерность доски
        end - конечная свободная клетка на доске
        new_pieces - список порядковых номеров клеток доски, на которых поставлены фигуры программно
        """
        l = len(new_pieces)#Получаем кол-во поставленных программно поставленных фигур
        step = 0 #Отступ для определения, какую фигуру надо сместить
        #Механизм определния, дошла ли определенная фигура до конца, 
        #т.е. если фигура 1 не дошла до конца, а фигура 2 дошла до конца, то позицию должна
        #сменить именно 1 фигура
        for i in range(l-1):
            if new_pieces[i] != end and new_pieces[i+1]==end:
                step = (i-l)
        if step == 0: #Если такого случая не нашлось, то выводим ничего
            return
        #Матрицу заменяем на соотвествующий фигуре клон
        wmatrix = [list(x) for x in wmatrix_clones[step+1]]
        #Берем координаты фигуры, которую перемещаем
        row = new_pieces[step]//n
        col = new_pieces[step]%n
        wmatrix[row][col] = "H" #Ставим на место этой фигуры флаг посещенности
        #Перезаписываем более младшие клоны под шаблон старшего:
        for mc in range(step+1, 0):
            wmatrix_clones[mc] = [list(x) for x in wmatrix]
        step = step + l
        
        #Механизм постановки фигуры на новое место
        for i in range(step, l-1):
            free_square = self.find_square(wmatrix, n, new_pieces[step])
            if free_square is not None:
                wmatrix_clones[i] = [list(x) for x in wmatrix]
                wmatrix = self.set_up_piece(wmatrix, free_square, n)
                new_pieces[i] = free_square
            else:
                break
        return wmatrix, wmatrix_clones, new_pieces

    
    #Основная функция, которая ставит фигуры изначально и перемещает "свободную" фигуру
    def working(self) -> tuple:
        """
        Параметры:
        wmatrix - матрица для консольного вывода
        n - размерность доски
        new_pieces - список порядковых номеров клеток доски, на которых поставлены фигуры программно
        condition_pieces - список координат фигур, которые поставлены условно
        cnt_of_my_pieces - кол-во фигур, которые ставятся программно
        cnt_of_condition_pieces - кол-во фигур, которые поставлены условно
        matrix_for_pg - доска визуального решения pygame
        figure - фигура, которую ставим на доску
        """
        self.wmatrix_clones = [0]*(len(self.new_pieces)-1) #Создание мест для матриц-клонов

        #Если нет фигур, которые надо ставить программно, то выводим единственное решение с условными фигурами
        if len(self.new_pieces) == 0:
            self.matrix_for_pg.draw(self.n)
            self.output()
            self.master.cnt+=1
            self.outputTheBoard = 1
            for i in range(self.n):
                print(self.wmatrix[i])
            return
        
        #Первая постановка фигур на доску
        for i in range(len(self.new_pieces)-1):
            #Ищется свободное место
            free_square = self.find_square(self.wmatrix, self.n, 0)
            #Записывается клон-матрицы
            #Происходит до постановки фигуры для того, чтобы было куда откатываться
            self.wmatrix_clones[i] = [list(x) for x in self.wmatrix]
            #Ставит фигуры на доску консольную и pygame
            self.wmatrix = self.set_up_piece(self.wmatrix, free_square, self.n)
            self.matrix_for_pg.set_up_piece_for_tkinter(free_square,self.n, (255,0,0), (0,0,255), self.figure)
            self.new_pieces[i] = free_square
        
        while self.new_pieces[0] != self.n**2 -1: #Пока самая старшая фигура не пройдет по всем клеткам
            free_square = self.find_square(self.wmatrix, self.n) #Определеяем свободное место для нашей "свободной" фигуры
            end = self.find_square(self.wmatrix, self.n, 0, "0", True) #Определяем, в какой клетке запускать step-back
            if free_square is not None: 
                #Если свободная клетка есть, то считаем ее как одно из решений
                #Необязательно физически ставить "свободную" фигуру на доску, можно просто засчитать как ход
                p_row = (free_square//self.n)
                p_col = (free_square%self.n)
                for row in range(p_row, self.n):
                    if row > p_row:
                            p_col = 0
                    for col in range(p_col, self.n):
                        if self.wmatrix[row][col] == "0":
                            self.new_pieces[-1] = row*self.n+col
                            self.master.cnt+=1
                            self.output() #Вывод решения в файл
                            if self.outputTheBoard == False:
                                #Вывод первого полноценного решения, вместе со "свободной" фигурой на доски
                                self.matrix_for_output = [list(x) for x in self.wmatrix]
                                self.matrix_for_output = self.set_up_piece(self.matrix_for_output, self.find_square(self.matrix_for_output, self.n), self.n)
                                self.matrix_for_pg.set_up_piece_for_tkinter(self.find_square(self.wmatrix, self.n),self.n, (255,0,0), (0,0,255), self.figure)
                                for i in range(self.n):
                                    print(self.matrix_for_output[i])
                                self.outputTheBoard = True
                                self.matrix_for_pg.draw(self.n)

            else:
                #Проверка на то, какая фигура достигла конца
                index_of_end = self.count_of_pieces()-(self.k+self.l)
                for i in range(index_of_end+1, -1, -1):
                    #Перемещаю все более младшие фигуры в фактический конец доски (n*n)-1
                    self.new_pieces[index_of_end]=self.n**2-1
                end = self.new_pieces[index_of_end]

            #Запуск отступа
            ret_step_back = self.step_back(self.wmatrix, self.wmatrix_clones, self.n, end, self.new_pieces)
            if ret_step_back is None:
                return
            else:
                self.wmatrix, self.wmatrix_clones, self.new_pieces = ret_step_back

    def set_up_piece(self, wmatrix:list, pos: int, n: int,  piece = "#") -> list:
        """
        Параметры:
        wmatrix - матрица консольного вывода
        pos - порядковый номер клетки, куда ставить фигуру
        n - размерность доски
        piece - как обозначать фигурку на доске
        """
        if pos is not None:#Если позиция была передана без ошибок
            #Переводим порядковый номер в координаты
            row = (pos//n)
            col = (pos%n)
            #Если в этом месте не свободно, то выводим "no solution" и закрываем программу с ошибкой
            if wmatrix[row][col] != "0":
                self.master.output_message("no solution")
                self.master.f.close()
                raise exceptions.FigureException("Ошибка! Фигура не может быть помещена.")
            
            wmatrix[row][col] = piece #Ставим фигуру на доску
            #Реализация боя фигуры King-Horse
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
        
    def find_square(self, wmatrix: list, n:int, previous_free_square=0, square = "0", reverse = False) -> int:
        """
        Параметры:
        wmatrix - матрица консольного вывода
        n - размерность доски
        previous_free_square - номер свободной клетки из предыдущей итерации
        square - что конкретно нужно найти
        reverse - начинать ли с конца? (Аналогично тому, чтобы искать последнюю необходимую клетку)
        """
        #Переводим порядковый номер в координаты
        p_row = (previous_free_square//n)
        p_col = (previous_free_square%n)
        #разворот для поиска конечного значения
        if reverse:
            wmatrix = [x[::-1] for x in wmatrix][::-1]
        #запись координаты клетки
        k = -1
        #Небольшая оптимизация, например, предыдущая свободная клетка была (4, 3), то поиск надо начинать с нее
        #Однако в следующей строчке надо начинать поиск уже с самого начала, а не с 4, поэтому p_col переводим в 0
        for row in range(p_row, n):
            if row > p_row:
                    p_col = 0
            for col in range(p_col, n):
                if wmatrix[row][col] == square: #Нашли ближащую клетку и вернули ее
                    k = (row*n)+col
                    if reverse:
                        return n*n-1-k
                    return k
        
        if reverse and k == -1:
            return self.find_square(wmatrix, n, 0, "#", )
        elif k == -1:
            return None
        
    #Функция проходится по доске и считает поставленные фигурки
    def count_of_pieces(self): 
        cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.wmatrix[i][j] == "#":
                    cnt+=1
        return cnt

        
        #Если свободной клетки не нашло, то автоматически возвращается None

def main():
    figure = kh_figure
    f = open("Output_Lab_2.txt", "w")
    game = Game(figure, f)
    game.start()

if __name__ == "__main__":
    main()
    