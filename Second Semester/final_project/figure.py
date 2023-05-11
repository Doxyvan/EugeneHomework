import exceptions
from abc import ABC, abstractmethod

class Figure(ABC):
    #Абстрактный класс для кастомных фигур
    #Метод принимает в себя номер позиции фигуры на доске
    @abstractmethod
    def __init__(self, pos) -> None:
        self.pos = pos


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
        if cells[row*n+col][0] != (255,255,255): #Вся доска изначально белая, поэтому свободные клетки обозначаются белым 
            raise exceptions.FigureException("Ошибка! Фигура не может быть помещена.")

        #Цикл для постановки фигуры на доску
        for i in range(5):
            if i%2==0:
                for m in range(-1,2,2):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m][0] = color_for_bites
            else:
                for m in range(-2,3):
                    if n>row+(i-2) >= 0 and n>col+m>=0:
                        cells[(row+(i-2))*n+col+m][0] = color_for_bites
                    
        #Обозначение фигуры на доске
        cells[row*n+col][0] = color_for_figure
        return cells