"""
1) Напишите программу, которая случайным образом выбирает целое число от 1 до 100.
Ваша программа должна запрашивать у пользователя догадки — если пользователь угадывает неправильно, 
она должна печатать, является ли догадка слишком высокой или слишком низкой. Если пользователь угадывает правильно,
программа должна вывести количество догадок, сделанных пользователем, чтобы угадать правильный ответ. 
Вы можете предположить, что пользователь введет правильный ввод.
2) Вы должны создать класс, который будет принимать экземпляр класса Tk().
3) Должны быть три кнопки:
·   Ввод значения 
·   Начать заново 
·   Вывод сообщения o количестве попыток
4) Должна быть надпись o догадках куда следовать (верх, вниз, правильный ответ)
5) Значение выбирается рандомно
6) Ввод строки, где будет проверяется правильность введенного значения 
(тут нужно быть внимательнее и проверять, на то чтобы буквы не вводились и  небыло выхода за границы поиска) 

"""
import tkinter as tk
from random import randint
class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.start = tk.Button(self,text="Ввод значения", command=self.Start)
        self.restart = tk.Button(self,text="Начать заново", command=self.Restart)
        self.print_cnt = tk.Button(self,text="Вывод сообщения о количестве попыток", command=self.Print_cnt)

        self.start.grid(column=1,row=1)
        self.restart.grid(column=2,row=1)
        self.print_cnt.grid(column=3,row=1)

        self.cnt = 0
        self.goal = 0
    def Start(self):
        self.goal = randint(0,100)
        SW = Start_Window(self)
        SW.wait_window()
    def Restart(self):
        self.goal = randint(0,100)

    def Print_cnt(self):
        PC = Print_Cnt(self)
        PC.wait_window()

class Start_Window(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        vcmd = (self.register(self.validate_entry), "%P")


        self.main_label = tk.Label(self, text="Введите число, которое я загадал!")
        self.ready_button = tk.Button(self,text="Готово", command = self.game)
        self.exit_button = tk.Button(self,text="Выход", command = self.destroy)
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)

        
        self.main_label.grid(column=1,row=1,columnspan=2)
        self.entry.grid(column=1,row=2,columnspan=2)
        self.ready_button.grid(column=1,row=3)
        self.exit_button.grid(column=2,row=3)

        

    def game(self):
        self.master.cnt +=1
        num = int(self.entry.get())
        goal = self.master.goal
        if num > goal:
            self.main_label["text"] = "Мое число меньше, чем ваше!"
        elif num < goal:
            self.main_label["text"] = "Мое число больше, чем ваше!"
        else:
            self.main_label["text"] = "Вы угадали!"
            self.master.Print_cnt()

    def validate_entry(self, entry):
        alp = ["0", "1", "2", "3", "4", "5", "6", "7","8","9"]
        #Проверка на отсутствие недопустимых символов в строке
        for i in entry:
            if i not in alp:
                return False
        #Проверка на соблюдение границ
        if len(entry):
            if int(entry) > 100 or int(entry)<0:
                return False

        return True
class Print_Cnt(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self,text="Количество попыток: "+str(master.cnt))
        self.exit_button = tk.Button(self,text="Выход", command = self.destroy)

        self.label.grid(column=1,row=1)
        self.exit_button.grid(column=1,row=2)


def main():
    MW =Main_Window()
    MW.mainloop()
if __name__=="__main__":
    main()