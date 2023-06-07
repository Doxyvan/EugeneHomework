from abc import ABC, abstractmethod
import tkinter as tk

class Figure(ABC):
    #Абстрактный класс для кастомных фигур
    #Метод принимает в себя номер позиции фигуры на доске
    @abstractmethod
    def __init__(self, pos) -> None:
        ...


    """Метод, принимающий в себя четыре параметра:
    n - размерность доски
    cells - словарь, где ключом является номер клетки, а значением является кортеж типа ((цвет), (координаты для отрисовки)),
    является интерпритацией доски для pygame
    color_for_figure - цвет для фигуры
    color for bites - цвет для обозначения удара фигуры
    """
    @abstractmethod
    def set_up_figure(self, n:int, cells:dict, color_for_figure:tuple, color_for_bites:tuple) -> tuple:
        ...


class King_Horse(Figure):
    def __init__(self, pos:int) -> None:
        #pos - номер клетки в матрице
        self.pos = pos

    def set_up_figure(self, n:int, cells:dict, color_for_figure:tuple, color_for_bites:tuple) -> tuple:
        """
        Параметры:
        n - размерность доски
        cells - словарь, где содержатся параметры каждой клетки в матрице для pygame
        color_for_figure - цвет для обозначения фигуры
        color_for_bites - цвет для обозначения ударов фигуры
        """
        row = (self.pos//n) #Строка
        col = (self.pos%n)#Столбец
        #Цикл для постановки фигуры на доску
        for i in range(5):
            if i%2==0:
                for m in range(-1,2,2):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m] = color_for_bites
            else:
                for m in range(-2,3):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m] = color_for_bites
                    
        #Обозначение фигуры на доске
        cells[row*n+col] = color_for_figure
        return cells
    

class Circle(Figure):
    def __init__(self, pos:int) -> None:
        #pos - номер клетки в матрице
        self.pos = pos

    def set_up_figure(self, n:int, cells:dict, color_for_figure:tuple, color_for_bites:tuple) -> tuple:
        """
        Параметры:
        n - размерность доски
        cells - словарь, где содержатся параметры каждой клетки в матрице для pygame
        color_for_figure - цвет для обозначения фигуры
        color_for_bites - цвет для обозначения ударов фигуры
        """
        row = (self.pos//n) #Строка
        col = (self.pos%n)#Столбец
        #Цикл для постановки фигуры на доску
        for i in range(5):
            if i%2==0:
                for m in range(-1,2,2):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m] = color_for_bites
            else:
                for m in range(-2,3,2):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m] = color_for_bites
                    
        #Обозначение фигуры на доске
        cells[row*n+col] = color_for_figure
        return cells
    
class Vizier(Figure):
    def __init__(self, pos:int) -> None:
        #pos - номер клетки в матрице
        self.pos = pos

    def set_up_figure(self, n:int, cells:dict, color_for_figure:tuple, color_for_bites:tuple) -> tuple:
        """
        Параметры:
        n - размерность доски
        cells - словарь, где содержатся параметры каждой клетки в матрице для pygame
        color_for_figure - цвет для обозначения фигуры
        color_for_bites - цвет для обозначения ударов фигуры
        """
        row = (self.pos//n) #Строка
        col = (self.pos%n)#Столбец
        #Цикл для постановки фигуры на доску
        for i in range(5):
            if i!=2:
                m = 0
                if n>row+(i-2) >= 0 and n>col+m>=0:
                    cells[(row+(i-2))*n+col+m] = color_for_bites
            else:
                for m in range(-2,3):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m] = color_for_bites
                    
        #Обозначение фигуры на доске
        cells[row*n+col] = color_for_figure
        return cells

class Game_Box(tk.Toplevel):
    def __init__(self, n:int, master) -> None:
        """
        Параметры:
        n - размерность доски
        window_width - ширина квадратного окна для pygame
        border - расстояние между клеточками
        """
        super().__init__(master)
        self.matrix = dict()
        self.cell_list = [0]*n**2
        for i in range(n):
            for j in range(n):
                cell =tk.Button(self, text="", height=5, width=10, background="white", state="disabled")
                cell.grid(row=i, column=j)
                self.matrix[i*n+j] = cell
                

    
    #Постановка фигуры на поле
    def set_up_piece_for_tkinter(self, pos: int, n: int, color_for_figure:tuple, color_for_bite:tuple, figure) -> list:
        """
        Параметры
        pos - номер клетки на доске, куда ставить фигуру
        n - размерность доски
        color_for_figure - цвет для фигуры
        color_for_bite - цвет для ударов фигуры
        figure - ссылка на фигуру, которая будет ставиться 
        """
        #Очищение поля перед постановкой фигуры
        for i in range(n):
            for j in range(n):
                self.cell_list[i*n+j] = "white"
        #Постановка фигуры
        if pos is not None:
            self.cell_list = figure(pos).set_up_figure(n, self.cell_list, color_for_figure, color_for_bite)

    def draw(self, n: int) -> None:
        for i in range(n):
            for j in range(n):
                self.matrix[i*n+j]["background"] = self.cell_list[i*n+j]


class Main_Menu(tk.Tk):
    "Содержит меню вида [Название фигуры] - [Кнопка]"
    def __init__(self) -> None:
        super().__init__()
        self.label_King_Horse = tk.Label(text="Король-Конь")
        self.button_King_Horse = tk.Button(text="Поставить", command = lambda: [self.set_up(King_Horse)])

        self.label_Circle = tk.Label(text="Кружочек")
        self.button_Circle = tk.Button(text="Поставить", command = lambda:[self.set_up(Circle)])

        self.label_Vizier = tk.Label(text="Визирь")
        self.button_Vizier  = tk.Button(text="Поставить", command = lambda:[self.set_up(Vizier)])

        self.label_King_Horse.grid(column=1, row=1)
        self.button_King_Horse.grid(column=1, row=2)

        self.label_Circle.grid(column=2, row=1)
        self.button_Circle.grid(column=2, row=2)

        self.label_Vizier.grid(column=3, row=1)
        self.button_Vizier.grid(column=3, row=2)

        self.n = 11 #Не стоит это менять
        self.MW = Game_Box(self.n, self)

    def set_up(self, figure):
        
        center = int(self.n*(self.n-1)/2)+int(self.n/2)
        self.MW.set_up_piece_for_tkinter(center, self.n, "red", "blue", figure)
        self.MW.draw(self.n)


def main():
    MM = Main_Menu()
    MM.mainloop()

if __name__ == "__main__":
    main()
    