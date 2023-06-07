from abc import ABC, abstractclassmethod
from typing import Any
from typing_extensions import Literal
import tkinter as tk


class Triangle(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.label = tk.Label(self, text="Введите 3 стороны через пробел")
        self.entry = tk.Entry(self)
        self.canvas = tk.Canvas(self, bg="white", width=300, height=300)
        self.button = tk.Button(self, text="Готово", command=self.draw)
        self.area = tk.Label(self, text="Площадь фигуры = ")

        self.label.grid(row=1,column=1)
        self.entry.grid(row=2,column=1)
        self.button.grid(row=3,column=1)
        self.canvas.grid(row=4,column=1)
        self.area.grid(row=5, column=1)
        

    def draw(self):
        start = 50
        size =10
        data = list(map(int, self.entry.get().split()))
        sides = [abs(data[0]), abs(data[1]), abs(data[2])]
        a = sides.pop(sides.index(min(sides)))
        b = sides.pop(sides.index(min(sides)))
        c = sides.pop(sides.index(min(sides)))
        if a+b>c and a+c>b and c+b>a:
            perimetr = (a+b+c)/2
            area = (perimetr*(perimetr-(a))*(perimetr-(b))*(perimetr-(c)))**0.5
            xb = abs(round((c**2 - b**2 - a**2)/(2*a), 0))
            yb = abs(round((b**2 - xb**2)**0.5, 0))
            self.canvas.create_rectangle(0, 0, 400, 400, fill="white")
            self.canvas.create_polygon(start, start, start+a*size, start,  start+xb*size,  start+yb*size)
            self.area["text"]= "Площадь фигуры = " + str(area)
        else:
            self.area["text"]= "Такой треугольник не может быть создан! Нарушено основное неравенство треугольников"

class Square(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.label = tk.Label(self, text="Введите сторону")
        self.entry = tk.Entry(self)
        self.canvas = tk.Canvas(self, bg="white", width=300, height=300)
        self.button = tk.Button(self, text="Готово", command=self.draw)
        self.area = tk.Label(self, text="Площадь фигуры = ")

        self.label.grid(row=1,column=1)
        self.entry.grid(row=2,column=1)
        self.button.grid(row=3,column=1)
        self.canvas.grid(row=4,column=1)
        self.area.grid(row=5, column=1)
        

    def draw(self):
        side = int(self.entry.get())
        self.canvas.create_rectangle(0, 0, 400, 400, fill="white")
        self.canvas.create_rectangle(150-side, 150-side, 150+side, 150+side)

        self.area["text"]= "Площадь фигуры = " + str(side*side)

class Circle(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.label = tk.Label(self, text="Введите радиус")
        self.entry = tk.Entry(self)
        self.canvas = tk.Canvas(self, bg="white", width=300, height=300)
        self.button = tk.Button(self, text="Готово", command=self.draw)
        self.area = tk.Label(self, text="Площадь фигуры = ")
        
        
        self.label.grid(row=1,column=1)
        self.entry.grid(row=2,column=1)
        self.button.grid(row=3,column=1)
        self.canvas.grid(row=4,column=1)
        self.area.grid(row=5, column=1)
        

    def draw(self):
        radius = int(self.entry.get())
        self.canvas.create_rectangle(0, 0, 400, 400, fill="white")
        self.canvas.create_oval(150-radius, 150-radius, 150+radius, 150+radius)

        self.area["text"]= "Площадь фигуры = " + str(radius*3.14*radius)
        
class Main_Menu(tk.Tk):
    "Содержит меню вида [Название фигуры] - [Кнопка]"
    def __init__(self) -> None:
        super().__init__()
        self.label_Square = tk.Label(self, text="Квадрат")
        self.button_Square = tk.Button(self,text="Нарисовать", command = lambda: [self.draw(Square)])

        self.label_Circle = tk.Label(self,text="Круг")
        self.button_Circle = tk.Button(self,text="Нарисовать", command = lambda:[self.draw(Circle)])

        self.label_Triangle = tk.Label(self,text="Треугольник")
        self.button_Triangle  = tk.Button(self,text="Нарисовать", command = lambda:[self.draw(Triangle)])

        self.label_Square.grid(column=1, row=1)
        self.button_Square.grid(column=1, row=2)

        self.label_Circle.grid(column=2, row=1)
        self.button_Circle.grid(column=2, row=2)

        self.label_Triangle.grid(column=3, row=1)
        self.button_Triangle.grid(column=3, row=2)
    
    def draw(self, Figure):
        self.terminal = Figure(self)

def main():
    MM = Main_Menu()
    MM.mainloop()

if __name__ == "__main__":
    main()
    