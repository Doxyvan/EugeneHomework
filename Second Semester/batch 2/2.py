import tkinter as tk

class MainBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.main_list=[]
        self.list_creator = tk.Button(self, text="Создание списка", command=self.create_list)
        self.list_print = tk.Button(self, text="Вывод списка в консоль", command = self.print_list_to_cmd)
        self.list_write = tk.Button(self, text="Запись списка в файл", command = self.write_list_to_file)
        self.list_len = tk.Button(self, text = "Кол-во элементов в списке", command=self.len_list)
        self.list_add_elem = tk.Button(self, text = "Добавить элемент в список", command = self.add_elem_to_list)
        self.list_find_elem = tk.Button(self, text = "Поиск элемента в списке", command=self.find_elem)
        self.list_del_elem = tk.Button(self, text="Удаление элемента из списка", command = self.del_elem)
        self.exit = tk.Button(self, text = "Выход", command=self.destroy)

        self.list_creator.grid(column=1, row=1)
        self.list_print.grid(column=1, row=2)
        self.list_write.grid(column=1, row=3)
        self.list_len.grid(column=1, row=4)
        self.list_add_elem.grid(column=1, row=5)
        self.list_find_elem.grid(column=1, row=6)
        self.list_del_elem.grid(column=1, row=7)
        self.exit.grid(column=1, row=8)

    def find_elem(self):
        self.list_finder= List_Find_Elem(self)
        self.list_finder.wait_window()
    
    def del_elem(self):
        self.list_finder= List_Del_Elem(self)
        self.list_finder.wait_window()

    def create_list(self):
        self.main_list = []
        self.creator_box = List_Creator(self)
        self.creator_box.wait_window()
    
    def add_elem_to_list(self):
        self.additor_elem = List_Add_Elem(self)
        self.additor_elem.wait_window()
    
    def print_list_to_cmd(self):
        print(self.main_list)
    
    def write_list_to_file(self):
        f = open("output.txt", "w")
        [f.write(str(x)+ " ") for x in self.main_list]
        f.write("\n")
        f.close()

    def len_list(self):
        if self.main_list is not None:
            self.len_box = List_Len(self)
            self.len_box.wait_window()

    def write_data_to_list(self, data):
        for i in range(len(data)):
            try:
                data[i] = int(data[i])
            except:
                pass
            self.main_list.append(data[i])

class List_Find_Elem(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.vcmd = (self.register(self.validate_func), "%P")
        self.label = tk.Label(self, text="Введите элемент, который хотите найти")
        self.entry = tk.Entry(self, validate="key", validatecommand=self.vcmd)
        self.button = tk.Button(self,text="Готово", command=self.find_elem)
        self.label_answer = tk.Label(self, text=" ")
        self.exit_button = tk.Button(self, text="Выход",command=self.destroy)
        
        self.exit_button.grid(column=2, row=3)
        self.label.grid(column=1, row=1, columnspan=2)
        self.entry.grid(column=1,row=2,columnspan=2)
        self.button.grid(column=1,row=3)
        self.label_answer.grid(column=1, row=4, columnspan=2)

    def find_elem(self):
        elem = self.entry.get()
        if any(str(x) in elem for x in self.master.main_list):
            try: elem = int(elem)
            except: pass
            self.label_answer["text"] = "Индекс элемента: " + str(self.master.main_list.index(elem))
        else:
            self.label_answer["text"] = "Элемент не найден!"
        

    def validate_func(self, entry):
        if (entry.find(" ")!=-1):
            return False
        return True

class List_Del_Elem(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.vcmd = (self.register(self.validate_func), "%P")
        self.label = tk.Label(self, text="Введите элемент, который хотите удалить")
        self.entry = tk.Entry(self, validate="key", validatecommand=self.vcmd)
        self.button = tk.Button(self,text="Готово", command=self.find_elem)
        self.label_answer = tk.Label(self, text=" ")
        self.exit_button = tk.Button(self, text="Выход",command=self.destroy)
        
        self.exit_button.grid(column=2, row=3)
        self.label.grid(column=1, row=1, columnspan=2)
        self.entry.grid(column=1,row=2,columnspan=2)
        self.button.grid(column=1,row=3)
        self.label_answer.grid(column=1, row=4, columnspan=2)

    def find_elem(self):
        elem = self.entry.get()
        if any(str(x) in elem for x in self.master.main_list):
            try: elem = int(elem)
            except: pass
            del self.master.main_list[self.master.main_list.index(elem)]
            self.label_answer["text"] = "Элемент удален."
        else:
            self.label_answer["text"] = "Элемент не найден!"
        

    def validate_func(self, entry):
        if (entry.find(" ")!=-1):
            return False
        return True

class List_Creator(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.label = tk.Label(self, text="Введите элементы списка через пробел")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self,text="Готово", command=lambda:[master.write_data_to_list(self.entry.get().split()), self.destroy()])

        self.label.grid(column=1, row=1)
        self.entry.grid(column=1,row=2)
        self.button.grid(column=1,row=3)

class List_Add_Elem(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.vcmd = (self.register(self.validate_func), "%P")
        self.label = tk.Label(self, text="Введите элемент, который хотите добавить")
        self.entry = tk.Entry(self, validate="key", validatecommand=self.vcmd)
        self.button = tk.Button(self,text="Готово", command=lambda:[master.write_data_to_list(self.entry.get().split()), self.destroy()])

        self.label.grid(column=1, row=1)
        self.entry.grid(column=1,row=2)
        self.button.grid(column=1,row=3)
    def validate_func(self, entry):
        if (entry.find(" ")!=-1):
            return False
        return True
class List_Len(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        
        self.label = tk.Label(self, text = "Количество элементов в списке: " + str(len(master.main_list)))
        self.label.grid(column=1, row=1)


def main():
    box = MainBox()
    box.mainloop()

if __name__ == "__main__":
    main()
