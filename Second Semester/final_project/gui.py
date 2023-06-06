import re
import tkinter as tk
import pygame as pg



"""
Класс окна для ввода N, L, K вида:
Введите N:
_________
Введите L:
_________
Введите K:
_________
В поля ввода могут вводится исключительно положительные числа
"""
class NLK_Window(tk.Tk):
    def __init__(self) -> None:

        super().__init__()
        self.resizable(False, False)
        #Валидация
        self.pattern = re.compile("(^[0-9]+$|^$)") #Регулярное выражение для проверки вводимого значения
        vcmd = (self.register(self.validate_entry), "%P") #Функция для активации валидации

        #Блок для переменной N
        self.label_for_n = tk.Label(self,text="Введите N")
        self.label_for_n.pack(anchor="n", padx=6, pady=6)
 
        self.entry_for_n = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.entry_for_n.pack(anchor="n", padx=6, pady=6)

        #Блок для переменной L
        self.label_for_l = tk.Label(self,text="Введите L")
        self.label_for_l.pack(anchor="n", padx=6, pady=6)
 
        self.entry_for_l = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.entry_for_l.pack(anchor="n", padx=6, pady=6)

        #Блок для переменной K
        self.label_for_k = tk.Label(self,text="Введите K")
        self.label_for_k.pack(anchor="n", padx=6, pady=6)
 
        self.entry_for_k = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.entry_for_k.pack(anchor="n", padx=6, pady=6)

        #Блок для кнопки
        self.start_button = tk.Button(self,text="Запустить", command=self.create_coordinates_window)
        self.start_button.pack(anchor="n", padx=6, pady=6)

        #Координаты для фигур по условию
        self.x, self.y = [], []

    #Валидация данных через регулярные выражения
    def validate_entry(self, entry:str) -> None:
        return self.pattern.match(entry) is not None
    
    #Создания окна для ввода координат
    def create_coordinates_window(self) -> None: 
        #Проверяет, введены ли все значения и нет ли пустых строк
        if self.entry_for_n.get() and self.entry_for_l.get() and self.entry_for_k.get():
            #Берет значения в числовом формате
            self.n, self.l, self.k = int(self.entry_for_n.get()), int(self.entry_for_l.get()), int(self.entry_for_k.get())
            #Если k > 0, то запускается окно ввода координат
            if self.k>0:
                #Делаю невозможным взаимодействовать с окном ввода N-L-K
                self.start_button.configure(state="disabled")
                self.entry_for_k.configure(state="disabled")
                self.entry_for_n.configure(state="disabled")
                self.entry_for_l.configure(state="disabled")
                #Создаю окно ввода координат
                self.child_window = Coord_Input(self)
                #Ожидаю, пока окно не уничтожится
                self.child_window.wait_window()
                #Закрываю окно ввода N-L-K
                self.destroy()
            else:
                #Если K == 0, то закрываю ввода N-L-K
                self.destroy()
                
    #Метод, который забирает с окна ввода координат эти самые координаты
    def get_child_coords(self) -> None:
        #Проверка на то, что все координаты это два числа, записанные через пробел
        flag = True
        for i in range(self.k):
            if len(self.child_window.list_of_entries[i].get().split())!=2:
                flag=False

        #Если предыдущая проверка истина, то координаты записываются в соотвествующие переменные
        if flag:
            for i in range(self.k):
                x, y =  self.child_window.list_of_entries[i].get().split()
                self.x.append(int(x))
                self.y.append(int(y))
            #Закрываем окно ввода координат
            self.child_window.destroy()

    def get_coords(self)-> tuple[list]:
        return self.x, self.y
    
    def get_info(self)-> tuple[int]:
        return self.n, self.l, self.k


"""
Класс окна для ввода координат фигур по условию вида:
Введите координаты x, y: ____________________
Введите координаты x, y: ____________________
...
Введите координаты x, y: ____________________
По числу условных фигур K
В поля ввода могут вводится исключительно два положительных числа через единственный пробел
"""
class Coord_Input(tk.Toplevel):
    def __init__(self, master:NLK_Window) -> None:
        #master - владелец этого окна, т.е. родитель
        super().__init__(master)
        #Лист для сбора поля ввода
        self.list_of_entries = []
        self.resizable(False, False)
        #Функция валидации
        vcmd = (self.register(self.validate_entry), "%P")

        #Создание блоков label-entry по числу фигур по условию
        for i in range(master.k):
            label = tk.Label(self, text="Введите координаты x, y").grid(column=1, row=i+1)
            entry = tk.Entry(self, validate="key", validatecommand=vcmd)
            entry.grid(column=2, row=i+1)
            self.list_of_entries.append(entry)

        #Создание кнопки
        self.start_button = tk.Button(self,text="Запустить", command=master.get_child_coords)
        self.start_button.grid(row=master.k+1,columnspan=2, padx=6, pady=6)

    def validate_entry(self, entry:str) -> bool:
        #entry - строка, которая проверяется
        alp = ["0", "1", "2", "3", "4", "5", "6", "7","8","9", " "] #Доступные значения для ввода
        
        #Проверка на единственность пробела, который находится между двумя числами
        if " " in entry:
            if entry.count(" ") > 1 or entry.index(" ") == 0:
                return False 
        #Проверка на отсутствие недопустимых символов в строке
        for i in entry:
            if i not in alp:
                return False
        
        #Алгоритм смены числа если оно превышает возможное(n)
        #Например, если в пользователь хочет ввести координаты 10 100 при n = 20, то после проверки алгоритмом в строке будет стоять 10 19
        """for i in range(len(entry.split())):
            if int(entry.split()[i])>=self.master.n and i == 0:
                entry = str(self.master.n-1) + entry[len(entry.split()[i]):]
            elif int(entry.split()[i])>=self.master.n and i == 1:
                entry = entry[:-len(entry.split()[i])] + str(self.master.n-1)"""

        return True

"""
Класс окна для создания окна вывода искомых решений
"""
class PyGameWindow():
    def __init__(self, n:int, window_width=600, border = 1) -> None:
        """
        Параметры:
        n - размерность доски
        window_width - ширина квадратного окна для pygame
        border - расстояние между клеточками
        """
        super().__init__()
        
        #Параметры окна pygame
        self.window_width = window_width #Ширина квадратного окна
        self.window_height = window_width+20
        self.width=window_width//(n) - 1 #Размер квадратиков динамически подгоняется под окошко
        self.cell_list = dict() #Хранит информацию о клетках

        #Создание белой сетки
        for i in range(n):
            for j in range(n):
                self.cell_list[i*n+j] = [(255,255,255), (border+(self.width+border)*j, border+(self.width+border)*i, (self.width), (self.width))]
    
    #Постановка фигуры на поле
    def set_up_piece_for_tkinter(self, pos: int, n: int, color_for_figure:tuple, color_for_bite:tuple, figure) -> list:
        """
        Параметры
        pos - номер клетки на доске, куда ставить фигуру
        n - размерность доски
        color_for_figure - цвет для фигуры
        color_for_bite - цвет для ударов фигуры
        figure - фигура, которая будет ставиться
        """
        if pos is not None:
            self.cell_list = figure(pos).set_up_figure(n, self.cell_list, color_for_figure, color_for_bite)

    def draw(self, n: int) -> None:
        #n - размерность доски, на которой выводятся фигуры
        #Отрисовка первого решения через PyGame
        pg.init()#Инициализируем
        running = 1
        #создаем квадратное окошко размером window_width
        sc = pg.display.set_mode((self.window_width, self.window_height))
        
        #Вносим на доску фигуры
        for i in range(n):
            for j in range(n):
                pg.draw.rect(sc, self.cell_list[i*n+j][0], self.cell_list[i*n+j][1])
        #Отрисуем ниже на доске квадратик
        button = pg.Rect(self.window_width//2 - 40,self.window_height-19,80,19)
        pg.draw.rect(sc, (255,255,255), button)
        #Отрисуем текст на кнопке
        font = pg.font.SysFont(None, 24)
        img = font.render('start', True, (0,0,0))
        sc.blit(img, (self.window_width//2 - 20,self.window_height-17,40,17))
        #Отрисовываем доску один раз
        pg.display.flip() 
        #Ловим события на доске
        while running:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    # Определяем x, y нажатия на доске
                    x, y = event.pos
                    if button.collidepoint(x, y):
                        running = False