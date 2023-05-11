"""
Разберем суть алгоритма на примере доски 3x3 и 2 фигурах, которые помещены программно:
1. Рассмотрим пустое поле:
['0', '0', '0']
['0', '0', '0']
['0', '0', '0']
Как можно заметить, все клетки готовы к тому, чтобы поставить туда фигуру, для удобства перейдем из системы
(x, y) для каждой клетки к ее порядковому номеру, например, клетка (1, 2) в данном случае будет иметь порядковый
номер 7, а клетка (0,0) - 0. Таким образом за каждой клеткой зафиксирован ее номер от 0 до n-1 (в данном случае это 8).

2. Поставим 1 фигуру в первую свободную клетку, т.е. клетку 0
['#', '*', '0']
['*', '*', '*']
['0', '*', '0']
Можно заметить, что осталось 3 свободные клетки с номерами 2, 6 и 8. Т.к. первая фигура фиксирована к клетке 0,
то вторая без проблем может поставиться в свободные клетки, таким образом образовалось сразу 3 решения:
(0, 0) (2, 0)
(0, 0) (0, 2)
(0, 0) (2, 2)

3. Переместим первую фигуру в следующую свободную клетку
['Н', '*', '#']
['*', '*', '*']
['0', '*', '0']
Как можно заметить, посещенную ранее клетку отметили буковкой H (hidden - скрыта).
Это сделано для того, чтобы вторая фигура не приняла эту клетку за свободное место.
Если этого не сделать, то к нашим решениям добавится (0,0) (2,0), а такое уже было в предыдущем шаге.
Исходя из этого, второй фигуре остаются клетки с номерами 6 и 8. Мы нашли еще 2 решения:
(2,0) (0,2)
(2,0) (2,2)

4. Переместим первую фигуру в следующую свободную клетку
['Н', '*', 'Н']
['*', '*', '*']
['#', '*', '0']

Исходя из этого, второй фигуре остаются клетки с номером 8. Мы нашли еще 1 решения:
(0,2) (2,2)

Больше решений не будет, это очень похоже на задачу "Найти всевозможные пары элементов в последовательности"
Например, возьмем ряд чисел 1 2 3 4 5 и решим для этого ряда чисел поставленную задачу:
12, 13, 14, 15
23, 24, 25
34, 35
45
С каждым разом возможных пар становится все меньше и меньше, это делается во избежание повторений
(32 и 23 - одна и та же пара, поэтому в третьей строчке пара 23 отсутствует)

Для трех фигур (или цифр, если рассматривать на примере с рядами), алгоритм аналогичный:
"Найти всевозможные тройки элементов в последовательности"
Например, возьмем ряд чисел 1 2 3 4 5 и решим для этого ряда чисел поставленную задачу:
123 124 125 134 135 145
234 235 245
345

На примере вот ранее решенной задачи про пары элементов введу несколько обозначений,
необходимых для объяснения кода в дальнейшем, где слово "число" можно эквивалентно заменить на слово "фигура":
1. Разобьем числа по "старшинству" - условные индексы для чисел начиная с самого старшего (0) и
заканчивая самым младшим (l-1). Например, в паре 12 число "1" самое старшее, а число "2" - самое младшее.
2. Самое младшее число назовем "свободным", т.к. оно меняет свое положение каждое решение и 
не фиксируется на одном месте.
3. Для любого другого не "свободного" числа смена наступает тогда, 
когда его младший сосед доходит до крайней свободной клетки. 
Например, чтобы число "1" в паре 1X (где X - любое число, стоящее после числа "1") сменилось на число "2",
необходимо, чтобы его младший сосед, т.е. X, принял значение 5, после этого происходит смена числа.
Такая смена называется "отступ" или "step back"


Вернемся назад, чтобы определить, как именно возвращаться назад во времени и
переставлять определенную фигуру во времени. Для примера возьмем доску 3x3 и 3 фигуры программно:
0. Называть фигуры будем по их индексу от 0 до 2
1. Поставили нулевую фигуру
['#', '*', '0']
['*', '*', '*']
['0', '*', '0']
2. Поставили первую фигуру
['#', '*', '#']
['*', '*', '*']
['0', '*', '0']
Вторая фигура пройдется по двум оставшимся нулям и создаст соотвествующие решения, это уже разобрано.
Получается, чтобы получить новые решения, необходимо первую фигуру сместить на свободную клетку. Но что будет,
когда первая фигура дойдет до конечной свободной клетки?
['#', '*', 'Н']
['*', '*', '*']
['Н', '*', '#']
Такой исход не считается решением, но считается крайним случаем, после которого происходит step-back:
В такой ситуации следуют переместить следующую по старшинству фигуру, т.е. фигуру с индексом 0.
Но как это сделать, если первая фигура после себя оставляла флаги посещения "Н"?
Откатить доску до того момента, когда еще не существовало ни второй, ни первой фигуры.
Таким образом мы подходим к идее клонирования доски:
Откатим доску к шагу 1 и переместим фигуру 0 на следующую свободную клетку:
['Н', '*', '#']
['*', '*', '*']
['0', '*', '0']
Теперь можно повторить предыдущие шаги поставить оставшиеся фигуры.
Т.о. мы для каждой не "свободной" фигуры будем иметь клоны, чтобы откатывать время для нашей доски.
"""
import time
import pygame as pg
import exceptions
from gui import Game_Box, Box
from figure import King_Horse as kh_figure
from figure import Figure

#Функция для записи в файл определенного осообщения
def output_message(msg:str) -> None:
    #msg - сообщение, которое передаем в файл
    f.write(msg)
    f.write("\n")

#Функция для записи координат фигур определенного решения
def output(list_with_numbers: list, n: int, condition_pieces:tuple) -> None:
    """
    Параметры:
    list_with_numbers - список порядковых номеров клеток на доске, на которых стоят фигуры
    n - размерность доски
    condition_pieces - кортеж координат фигур, которые были поставлены из условия
    """
    for piece in condition_pieces: #Для фигур из условия
        f.write(str(piece[::-1])) #Запись происходит по виду (y, x) или (row, col)
    for piece in range(len(list_with_numbers)): #Для фигур, расставляемых программно
        t_row=(list_with_numbers[piece])//n
        t_col=(list_with_numbers[piece])%n
        coordinates = (t_row,t_col)
        f.write(str(coordinates))
    f.write("\n")

#Отступ для смены позиции очередной не "свободной" фигуры
def step_back(wmatrix: list, wmatrix_clones: list, n: int, end: int, new_pieces: list) -> tuple:
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
        free_square = find_free_square(wmatrix, n, new_pieces[step])
        if free_square is not None:
            wmatrix_clones[i] = [list(x) for x in wmatrix]
            wmatrix = set_up_piece(wmatrix, free_square, n)
            new_pieces[i] = free_square
        else:
            break
    return wmatrix, wmatrix_clones, new_pieces

#Основная функция, которая ставит фигуры изначально и перемещает "свободную" фигуру
def working(wmatrix: list, n: int, new_pieces: list, condition_pieces:tuple, cnt_of_my_pieces:int, cnt_of_condition_pieces:int, wmatrix_for_tkinter:Game_Box, figure:Figure) -> tuple:
    """
    Параметры:
    wmatrix - матрица для консольного вывода
    n - размерность доски
    new_pieces - список порядковых номеров клеток доски, на которых поставлены фигуры программно
    condition_pieces - список координат фигур, которые поставлены условно
    cnt_of_my_pieces - кол-во фигур, которые ставятся программно
    cnt_of_condition_pieces - кол-во фигур, которые поставлены условно
    wmatrix_for_tkinter - доска визуального решения pygame
    figure - фигура, которую ставим на доску
    """
    global outputTheBoard
    global cnt
    wmatrix_clones = [0]*(len(new_pieces)-1) #Создание мест для матриц-клонов

    #Если нет фигур, которые надо ставить программно, то выводим единственное решение с условными фигурами
    if len(new_pieces) == 0:
        wmatrix_for_tkinter.draw(n)
        output(new_pieces, n, condition_pieces)
        cnt+=1
        outputTheBoard = 1
        for i in range(n):
            print(wmatrix[i])
        return
    
    #Первая постановка фигур на доску
    for i in range(len(new_pieces)-1):
        #Ищется свободное место
        free_square = find_free_square(wmatrix, n, 0)
        #Записывается клон-матрицы
        #Происходит до постановки фигуры для того, чтобы было куда откатываться
        wmatrix_clones[i] = [list(x) for x in wmatrix]
        #Ставит фигуры на доску консольную и pygame
        wmatrix = set_up_piece(wmatrix, free_square, n)
        wmatrix_for_tkinter.set_up_piece_for_tkinter(free_square,n, (255,0,0), (0,0,255), figure)
        new_pieces[i] = free_square
    
    while new_pieces[0] != n*n -1: #Пока самая старшая фигура не пройдет по всем клеткам
        free_square = find_free_square(wmatrix, n) #Определеяем свободное место для нашей "свободной" фигуры
        end = find_last_free_square(wmatrix, n, 0) #Определяем, в какой клетке запускать step-back
        if free_square is not None: 
            #Если свободная клетка есть, то считаем ее как одно из решений
            #Необязательно физически ставить "свободную" фигуру на доску, можно просто засчитать как ход
            p_row = (free_square//n)
            p_col = (free_square%n)
            for row in range(p_row, n):
                if row > p_row:
                        p_col = 0
                for col in range(p_col, n):
                    if wmatrix[row][col] == "0":
                        new_pieces[-1] = row*n+col
                        cnt+=1
                        output(new_pieces, n, condition_pieces) #Вывод решения в файл
                        if outputTheBoard == False:
                            #Вывод первого полноценного решения, вместе со "свободной" фигурой на доски
                            matrix_for_output = [list(x) for x in wmatrix]
                            matrix_for_output = set_up_piece(matrix_for_output, find_free_square(matrix_for_output, n), n)
                            wmatrix_for_tkinter.set_up_piece_for_tkinter(find_free_square(wmatrix, n),n, (255,0,0), (0,0,255), figure)
                            for i in range(n):print(matrix_for_output[i])
                            outputTheBoard = True
                            wmatrix_for_tkinter.draw(n)

        else:
            #Проверка на то, какая фигура достигла конца
            index_of_end = count_of_pieces(wmatrix,n)-(cnt_of_condition_pieces+cnt_of_my_pieces)
            for i in range(index_of_end+1, -1, -1):
                #Перемещаю все более младшие фигуры в фактический конец доски (n*n)-1
                new_pieces[index_of_end]=n*n-1
            end = new_pieces[index_of_end]

        #Запуск отступа
        ret_step_back = step_back(wmatrix, wmatrix_clones, n, end, new_pieces)
        if ret_step_back is None:
            return
        else:
            wmatrix, wmatrix_clones, new_pieces = ret_step_back
    
def main():
    figure = kh_figure #Сюда давать ссылку на класс фигуры, активируется в gui.GameBox.set_up_piece_for_tkinter
    global cnt #Счет решений
    global f #Файл для записи решений
    global outputTheBoard #Вывелось ли решение на экран
    
    cnt = 0
    outputTheBoard = False
    f = open("Output_Lab_2.txt", "w")

    in_data = Box() #Создаем окно для ввода начальных значений
    in_data.wait_window() #Ждем отработки окна
    n, l, k = in_data.get_info() #Получаем информацию о поле и фигурах
    x, y = in_data.get_coords()  #Получаем координаты K-тых фигур
    in_data.mainloop() #Запускаем окно работать до закрытия
    
    #Если поле размерность 0x0, то и фигуру туда не поставить, а значит вывести "no solution"
    if n == 0: 
        output_message("no solution")
        f.close()
        return

    new_pieces = [-1]*l #Сюда будут записывать порядковые номера клеток, куда поставили фигуру в ходе решения

    wmatrix = matrix(n) #Создание консольной матрицы
    matrix_for_tkinter = Game_Box(n) #Создание матрицы pygame
    
    now = time.time() #Даем старт началу программы

    #Сюда будут записывать координаты клеток, куда поставили фигуру в условии
    #Именно координаты, потому что с этими клетками почти никаких действий и не производится
    condition_pieces = [] 
    
    #Постановка фигур по условию
    for index in range(k):
        condition_pieces.append((x[index],y[index])) #Запись координат фигур
        pos = y[index]*n + x[index] #Перевод координат в порядковый номер
        wmatrix = set_up_piece(wmatrix, pos, n) #Постановка в консольной матрице
        #Постановка в матрице pygame
        matrix_for_tkinter.set_up_piece_for_tkinter(pos, n, (0,255,0), (0, 0, 255), figure)
    
    #Запуск основной функции
    working(wmatrix, n, new_pieces, condition_pieces, l, k, matrix_for_tkinter, figure)
    
    f.close()#Закрываем файл
    end = time.time()#Получаем время окончания работы
    print(end-now)#Выводим время работы
    print(cnt)#Выводим кол-во ходов
#Функция создания консольной матрицы
def matrix(n):
    #n - размерность доски
    wmatrix = []
    row = ["0"] * n #Создаем строчку
    for _ in range(n):
        wmatrix.append([x for x in row]) #Множим эту строчку по числу n
        
    return wmatrix

#Функция для постановки фигуры на консольную доску
def set_up_piece(wmatrix: list, pos: int, n: int,  piece = "#") -> list:
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
            output_message("no solution")
            f.close()
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

#Функция для поиска следующей свободной клетки
def find_free_square(wmatrix: list, n:int, previous_free_square=0) -> int:
    """
    Параметры:
    wmatrix - матрица консольного вывода
    n - размерность доски
    previous_free_square - номер свободной клетки из предыдущей итерации
    """
    #Переводим порядковый номер в координаты
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    #Небольшая оптимизация, например, предыдущая свободная клетка была (4, 3), то поиск надо начинать с нее
    #Однако в следующей строчке надо начинать поиск уже с самого начала, а не с 4, поэтому p_col переводим в 0
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if wmatrix[row][col] == "0": #Нашли ближащий 0 и вернули его
                return (row*n)+col
    #Если свободной клетки не нашло, то автоматически возвращается None


#Аналогично функции find_free_square(), но ищет не первую, а последнюю свободную клетку
def find_last_free_square(wmatrix:list, n:int, previous_free_square=0) -> int:
    """
    Параметры:
    wmatrix - матрица консольного вывода
    n - размерность доски
    previous_free_square - номер свободной клетки из предыдущей итерации
    """
    k = -1
    p_row = (previous_free_square//n)
    p_col = (previous_free_square%n)
    for row in range(p_row, n):
        if row > p_row:
                p_col = 0
        for col in range(p_col, n):
            if wmatrix[row][col] == "0":
                k = (row*n)+col
    if k == -1: #Если свободной клетки не нашлось, то ищем последнюю поставленную фигуру
        return find_last_piece_square(wmatrix, n, 0)
    return k #Если нашлась свободная клетка, то ее выводим

#Функция проходится по доске и считает поставленные фигурки
def count_of_pieces(wmatrix: list, n:int): 
    """
    Параметры:
    wmatrix - матрица консольного вывода
    n - размерность доски
    """
    cnt = 0
    for i in range(n):
        for j in range(n):
            if wmatrix[i][j] == "#":
                cnt+=1
    return cnt

#Функция, аналогичная find_last_free_square(), только вместо свободной клетки ищет фигуру
def find_last_piece_square(wmatrix: list, n: int, previous_free_square=0) -> int:
    """
    Параметры:
    wmatrix - матрица консольного вывода
    n - размерность доски
    previous_free_square - номер свободной клетки из предыдущей итерации
    """
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
    
    