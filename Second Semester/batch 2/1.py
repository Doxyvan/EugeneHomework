from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
class Calculator:

    def __init__(self, master:'Tk'):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiplication_button = Button(master, text="*", command=lambda: self.update("multiplication"))
        self.division_button = Button(master, text="/", command=lambda: self.update("division"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.multiplication_button.grid(row=2, column=2)
        self.division_button.grid(row=2, column=3)
        self.reset_button.grid(row=2, column=4, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "division":
            if self.entered_number == 0:
                raise ZeroDivisionError()
            self.total /= self.entered_number
        elif method == "multiplication":
            self.total *= self.entered_number
        else: # reset
            self.total = 0
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

def main():
    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()
if __name__ == "__main__":
    main()
